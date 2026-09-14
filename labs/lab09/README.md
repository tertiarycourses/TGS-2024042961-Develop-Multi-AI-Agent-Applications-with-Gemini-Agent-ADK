# Lab 9 — Workflow Agents — Sequential, Parallel, Loop and Agent-as-a-Tool

**Topic 02:** Build A Multi Agent App with Gemini ADK  
**Learning outcome:** LO3 / LO2 — orchestrate multi-agent workflows with all four ADK collaboration patterns.  
**Tools:** google-adk, SequentialAgent, ParallelAgent, LoopAgent, AgentTool, output_key, google_search

## Goal

Work through the four ADK workflow patterns on realistic systems: a SequentialAgent travel planner, a ParallelAgent market-research desk with a synthesis step, a LoopAgent writer/critic refinement cycle, and an AgentTool bilingual report writer. The lab makes the decisive distinction explicit — when order is enforced by code vs by the model, and when a specialist takes control (handoff) vs returns a result (AgentTool).

## What you'll build

lab09 — four runnable multi-agent systems: agent.py (sequential travel planner), agent_parallel.py (market research), agent_loop.py (copy refinement), agent_as_tool.py (bilingual report writer).

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
uv run adk run lab09     # terminal chat
uv run adk web              # browser IDE, then pick lab09 at http://localhost:8000
```

## Agent scripts in this lab

- `agent.py` — the default agent loaded by `adk run lab09`
- `agent_as_tool.py` — Lab 09d — Agent-as-a-Tool: A Report Writer with Specialist Services
- `agent_loop.py` — Lab 09c — Loop Workflow: A Writer / Critic Refinement Cycle
- `agent_parallel.py` — Lab 09b — Parallel Workflow: A Market Research Desk

Open `uv run adk web` and select the script you want to run.

## Step-by-step

1. Read the sequential pipeline and note how output_key feeds the next instruction

   ```bash
   cat lab09/agent.py
   ```

2. Launch the web IDE and select lab09

   ```bash
   uv run adk web
   ```

3. Plan a trip and watch the three stages run in a guaranteed order

   ```bash
   Plan a 4-day trip to Tokyo
   ```

4. Read the parallel fan-out and explain why the three analysts need no ordering

   ```bash
   cat lab09/agent_parallel.py
   ```

5. Run the market research desk and compare its latency with the sequential pipeline

   ```bash
   Research Grab Holdings
   ```

6. Read the loop and find BOTH stopping conditions — max_iterations and escalate

   ```bash
   cat lab09/agent_loop.py
   ```

7. Run the refinement loop and count the iterations before approval

   ```bash
   Write landing page copy for a smart water bottle
   ```

8. Read the AgentTool example and state how tools=[AgentTool(...)] differs from sub_agents=[...]

   ```bash
   cat lab09/agent_as_tool.py
   ```

## Test it

The travel planner produces research, itinerary and budget in that fixed order; the research desk shows three analysts running concurrently before one synthesis; the loop stops early on approve_copy or at 3 iterations; and the report writer calls both specialists without ever transferring control.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
