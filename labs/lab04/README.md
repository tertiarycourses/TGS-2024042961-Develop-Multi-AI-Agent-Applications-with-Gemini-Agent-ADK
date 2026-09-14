# Lab 4 — Swap the Model — Running an ADK Agent on a Non-Gemini LLM

**Topic 01:** Overview of Agentic AI in Gemini ADK  
**Learning outcome:** LO2 / LO4 — compare models and assess the trade-offs for an engineering process.  
**Tools:** google-adk, LiteLlm, Gemini 3.8 Flash, OpenAI GPT-4.1-mini

## Goal

Use the LiteLlm wrapper to point the same agent at an OpenAI model, then compare it with Gemini on the same prompts to judge quality, latency and cost.

## What you'll build

lab04 — one agent definition that runs on either Gemini or an OpenAI model by changing a single line.

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
uv run adk run lab04     # terminal chat
uv run adk web              # browser IDE, then pick lab04 at http://localhost:8000
```

## Step-by-step

1. Inspect how LiteLlm wraps a non-Google model

   ```bash
   cat lab04/agent.py
   ```

2. Add your OpenAI key to labs/.env

   ```bash
   echo 'OPENAI_API_KEY=your-openai-key' >> .env
   ```

3. Run the agent on the OpenAI model

   ```bash
   uv run adk run lab04
   ```

4. Ask a reasoning question and note the answer quality and response time

   ```bash
   Explain in three sentences why an agent needs tools.
   ```

5. Edit lab04/agent.py and replace the model with a Gemini model string

   ```bash
   model='gemini-3.8-flash'
   ```

6. Re-run the identical prompt on Gemini

   ```bash
   uv run adk run lab04
   ```

7. Record quality, latency and cost for both in a comparison table

## Test it

The same agent runs unchanged on both providers, and you can state which model you would choose for this workload and justify it on quality, latency and cost.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
