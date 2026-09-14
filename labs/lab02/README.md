# Lab 2 — Build Your First ADK Agent — A Retail Banking Assistant

**Topic 01:** Overview of Agentic AI in Gemini ADK  
**Learning outcome:** LO1 / LO3 — define an agent from a model, name, description and instruction.  
**Tools:** google-adk, Gemini 3.8 Flash, adk run, adk web

## Goal

Create a single-agent banking customer-service assistant. You learn the four fields that define every ADK agent and see how the instruction alone shapes tone, scope and refusals.

## What you'll build

lab02 — a Gemini-powered banking assistant that answers general banking questions and refuses to handle PINs, OTPs or full account numbers.

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
uv run adk run lab02     # terminal chat
uv run adk web              # browser IDE, then pick lab02 at http://localhost:8000
```

## Step-by-step

1. Inspect the agent definition and note the four required fields

   ```bash
   cat lab02/agent.py
   ```

2. Identify model, name, description and instruction in the Agent(...) call

3. Run the agent in the terminal

   ```bash
   uv run adk run lab02
   ```

4. Ask an in-scope question

   ```bash
   How do I reset my internet banking password?
   ```

5. Ask an out-of-scope question and observe the guarded refusal

   ```bash
   What is my account PIN?
   ```

6. Launch the browser IDE and re-run the same prompts

   ```bash
   uv run adk web
   ```

7. Open http://localhost:8000, select lab02, and inspect the Events tab

8. Edit the instruction to make the assistant reply only in formal English, then re-run

## Test it

The agent answers general banking questions helpfully but declines to disclose or request a PIN, OTP or full account number, and the Events tab shows one LLM call per turn.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
