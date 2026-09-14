"""Lab 18 — Capstone starter.

Design and build your own multi-agent application for a use case in your
industry. This file is a scaffold: replace the specialists and the tool with
your own, then run it with:

    uv run adk run lab18
    uv run adk web

Requirements (see README.md):
  - at least THREE agents (one coordinator + two or more specialists)
  - at least TWO tools
  - session memory so it handles multi-turn conversations
  - a guardrail or a structured output schema
"""
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the labs/ root (one .env for all labs)
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from google.adk.agents import Agent

MODEL = "gemini-3.1-flash-lite"


# ---------- TOOLS ----------
def lookup_reference(topic: str) -> dict:
    """Looks up an internal reference note for a topic.

    Replace this with a real tool for your use case — an API call, a database
    query, or a calculation.

    Args:
        topic (str): The topic to look up.

    Returns:
        dict: status and result or error msg.
    """
    notes = {
        "refund": "Refunds are processed within 7 working days.",
        "delivery": "Standard delivery is 2-3 working days islandwide.",
    }
    hit = notes.get(topic.strip().lower())
    if not hit:
        return {"status": "error", "error_message": f"No reference note for {topic!r}."}
    return {"status": "success", "report": hit}


# ---------- SPECIALIST AGENTS ----------
# TODO: replace these two with the specialists your use case needs.
first_specialist = Agent(
    name="first_specialist",
    model=MODEL,
    description=(
        "Handles the first category of request. Rewrite this description — it is "
        "what the coordinator reads when deciding whether to route here."
    ),
    instruction=(
        "You are a specialist. State your role, your rules and your tone here. "
        "Use the lookup_reference tool when the user asks about a policy."
    ),
    tools=[lookup_reference],
)

second_specialist = Agent(
    name="second_specialist",
    model=MODEL,
    description="Handles the second category of request. Rewrite this description.",
    instruction="You are a second specialist. Describe your role and rules here.",
)


# ---------- COORDINATOR ----------
root_agent = Agent(
    name="root_agent",
    model=MODEL,
    description="Coordinator that routes each request to the right specialist.",
    instruction=(
        "You are a helpful coordinator. Greet the user, understand what they need, "
        "and transfer to the specialist whose description best matches the request. "
        "If nothing matches, answer briefly yourself."
    ),
    sub_agents=[first_specialist, second_specialist],
)
