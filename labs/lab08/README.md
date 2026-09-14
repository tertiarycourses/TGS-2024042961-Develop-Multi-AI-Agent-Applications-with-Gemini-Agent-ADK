# Lab 8 — Coordinator / Dispatcher — A Customer Support Desk

**Topic 02:** Build A Multi Agent App with Gemini ADK  
**Learning outcome:** LO3 — design a coordinator agent routing to specialised sub-agents.  
**Tools:** google-adk, sub_agents, coordinator/dispatcher pattern, function tools

## Goal

Build a production-shaped support desk where a triage agent dispatches each ticket to the billing, technical or returns specialist — each with its own instruction and its own tools against order and refund systems.

## What you'll build

lab08 — a triage coordinator with three tool-equipped specialists that routes real support tickets.

## Setup

Run every command from the `labs/` folder (the parent of this one), so that
the shared virtual environment and the single `.env` are picked up.

```bash
cd ..            # into labs/ if you are inside this lab folder
uv sync          # once per machine — installs google-adk and all deps
cp .env.example .env   # once — then paste your GOOGLE_API_KEY into .env
```

Then run this lab with either:

```bash
uv run adk run lab08     # terminal chat
uv run adk web              # browser IDE, then pick lab08 at http://localhost:8000
```

## Step-by-step

1. Read the three specialists, their tools and the triage coordinator

   ```bash
   cat lab08/agent.py
   ```

2. Compare the three descriptions and note how each states its routing trigger

3. Launch the web IDE and select lab08

   ```bash
   uv run adk web
   ```

4. Send a billing ticket and confirm it routes to billing_agent

   ```bash
   I was charged twice for order SG-10482
   ```

5. Send a technical ticket

   ```bash
   My wireless keyboard will not pair with my laptop
   ```

6. Send a returns ticket and watch the tool calls

   ```bash
   Where is order SG-10915 and can I still refund it?
   ```

7. Send a ticket that spans two queues and observe how triage resolves it

   ```bash
   My keyboard is faulty and I want my money back
   ```

8. Add a fourth specialist of your own to sub_agents and test the routing

## Test it

Each ticket reaches the matching specialist as a transfer_to_agent event, the returns ticket triggers lookup_order and check_refund_eligibility, and your fourth specialist routes.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
