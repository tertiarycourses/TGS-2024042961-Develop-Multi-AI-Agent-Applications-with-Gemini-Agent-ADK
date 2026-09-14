"""Lab 08 — Coordinator / Dispatcher: A Customer Support Desk.

A realistic support desk for an e-commerce company. One triage agent reads each
incoming ticket and dispatches it to the specialist that owns that queue —
billing, technical support, or returns & shipping.

Pattern: COORDINATOR / DISPATCHER (https://adk.dev/workflows/collaboration/).
The coordinator does no work itself; ADK generates a delegation tool from each
sub-agent's `description`, and routing quality depends entirely on how sharply
those descriptions are written.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the labs/ root (one .env for all agents)
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from google.adk.agents import Agent

import warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

google_api_key = os.environ.get("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables")

MODEL = "gemini-3.8-flash"


# ---------- TOOLS: the systems each specialist can actually query ----------

def lookup_order(order_id: str) -> dict:
    """Look up an order's status, items and shipping details.

    Args:
        order_id: The customer's order reference, e.g. "SG-10482".

    Returns:
        A dict with the order status, carrier and delivery estimate.
    """
    orders = {
        "SG-10482": dict(status="shipped", carrier="Ninja Van",
                         eta="2026-09-18", items="1x Wireless Keyboard",
                         total_sgd=89.00),
        "SG-10915": dict(status="processing", carrier="pending",
                         eta="2026-09-22", items="2x USB-C Hub",
                         total_sgd=134.00),
    }
    if order_id.upper() in orders:
        return dict(status="success", order=orders[order_id.upper()])
    return dict(status="error",
                message=f"No order found with reference {order_id}.")


def check_refund_eligibility(order_id: str, days_since_delivery: int) -> dict:
    """Check whether an order still falls inside the 14-day refund window.

    Args:
        order_id: The customer's order reference.
        days_since_delivery: Days elapsed since the order was delivered.

    Returns:
        A dict stating whether a refund is allowed and why.
    """
    if days_since_delivery <= 14:
        return dict(status="success", eligible=True,
                    message=f"Order {order_id} is within the 14-day window.")
    return dict(status="success", eligible=False,
                message=f"Order {order_id} is {days_since_delivery} days old; "
                        "the 14-day refund window has closed.")


# ---------- SPECIALIST AGENTS (the queues) ----------

billing_agent = Agent(
    name="billing_agent",
    model=MODEL,
    description=(
        "Handles payment and money questions: incorrect charges, duplicate "
        "payments, invoices, receipts, refund amounts and payment methods. "
        "Route here whenever the customer disputes or asks about money."
    ),
    instruction="""You are a billing specialist for an e-commerce company.

Use lookup_order to confirm the order total before discussing any charge.
Explain charges clearly and in plain language. If the customer is disputing an
amount, state what was actually charged and offer the next step.

Never promise a refund yourself — if the customer wants their money back,
say that the returns team must confirm eligibility first.
""",
    tools=[lookup_order],
)

technical_agent = Agent(
    name="technical_agent",
    model=MODEL,
    description=(
        "Handles product faults and technical problems: a device will not "
        "power on, will not pair or connect, firmware and driver issues, and "
        "setup help. Route here for anything broken or not working."
    ),
    instruction="""You are a technical support specialist for consumer electronics.

Diagnose methodically:
1. Ask what the customer has already tried, unless they have said.
2. Give numbered troubleshooting steps, simplest first.
3. If the steps cannot resolve it, say clearly that the unit needs replacement
   and that the returns team will handle the exchange.

Keep each reply under six steps so the customer is not overwhelmed.
""",
)

returns_agent = Agent(
    name="returns_agent",
    model=MODEL,
    description=(
        "Handles returns, exchanges, refund eligibility, shipping delays, "
        "lost parcels and delivery tracking. Route here for 'where is my "
        "order', 'I want to send this back' and 'can I get a refund'."
    ),
    instruction="""You are a returns and shipping specialist.

Use lookup_order to find the parcel's status and carrier before answering any
"where is my order" question.

Use check_refund_eligibility before confirming any refund. If you do not know
how many days have passed since delivery, ask the customer first.

State the outcome plainly: either the refund is approved and here are the
steps, or it is outside the window and here is the alternative.
""",
    tools=[lookup_order, check_refund_eligibility],
)


# ---------- THE COORDINATOR ----------

root_agent = Agent(
    name="support_triage_agent",
    model=MODEL,
    description="Front-desk triage agent that routes support tickets to the right specialist.",
    instruction="""You are the front desk of a customer support team.

Your ONLY job is to read the customer's message and dispatch it to the correct
specialist:

- billing_agent   — charges, invoices, payment disputes
- technical_agent — the product is faulty or will not work
- returns_agent   — returns, refunds, delivery and tracking

Rules:
- Do not attempt to solve the problem yourself.
- Greet the customer in one short sentence, then transfer.
- If a ticket covers two areas (e.g. a faulty item the customer wants to
  return), transfer to the one that unblocks the customer first, and say why.
- If the request fits none of the three queues, say what the team can help with.
""",
    sub_agents=[billing_agent, technical_agent, returns_agent],
)
