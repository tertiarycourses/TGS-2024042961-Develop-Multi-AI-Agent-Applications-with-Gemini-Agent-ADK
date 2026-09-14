# Lab 18 — Capstone — Build Your Own Multi-Agent Application

**Topic 04:** Build an Agentic AI App with Gemini Agent ADK and Streamlit  
**Learning outcome:** LO1 / LO2 / LO3 / LO4 — design a multi-agent solution and assess its feasibility.  
**Tools:** google-adk, sub_agents or SequentialAgent, custom tools, optional RAG and Streamlit

## Goal

In groups of three to five, design and build a multi-agent ADK application for a use case in your own industry, then present it with a feasibility assessment.

## What you'll build

A working multi-agent application with at least three agents, at least two tools, session memory and a documented feasibility assessment.

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
uv run adk run lab18     # terminal chat
uv run adk web              # browser IDE, then pick lab18 at http://localhost:8000
```

## Step-by-step

1. Form a group of three to five and choose an industrial use case from your own sector

2. Identify the specialist roles and draw the agent topology — coordinator or sequential

3. List the tools each agent needs and which are custom functions versus built-in

4. Build the agents, using the closest lab as your template

5. Add session memory so the application handles multi-turn conversations

6. Add a guardrail or a structured output schema appropriate to your use case

7. Test with at least five realistic prompts and record where the agent fails

8. Assess feasibility: accuracy, latency, token cost, maintainability and governance risk

9. Present the application and the feasibility assessment to the class in five minutes

## Test it

A running application with three or more agents and two or more tools, demonstrated live, plus a feasibility assessment stating whether you would recommend production deployment and on what evidence.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
