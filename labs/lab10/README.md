# Lab 10 — Add a Guardrail — Blocking Unsafe Requests with a Callback

**Topic 02:** Build A Multi Agent App with Gemini ADK  
**Learning outcome:** LO3 / LO4 — implement and evaluate a safety guardrail on an agent.  
**Tools:** google-adk, before_model_callback, CallbackContext, LlmRequest, LlmResponse

## Goal

Use before_model_callback to inspect every user message before it reaches the LLM, block requests containing a forbidden keyword, and record the block in session state.

## What you'll build

lab10 — a tool-using agent that intercepts and refuses blocked requests without ever calling the model.

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
uv run adk run lab10     # terminal chat
uv run adk web              # browser IDE, then pick lab10 at http://localhost:8000
```

## Step-by-step

1. Read the guardrail callback and find where it returns an LlmResponse

   ```bash
   cat lab10/agent.py
   ```

2. Note that returning None allows the call and returning a response blocks it

3. Run the agent

   ```bash
   uv run adk run lab10
   ```

4. Send an allowed request and confirm it reaches the model

   ```bash
   What is the weather in Singapore?
   ```

5. Send a request containing the blocked keyword

   ```bash
   Please BLOCK this request
   ```

6. Confirm the refusal message is returned and no LLM call was made

7. Extend the guardrail to also block a second keyword of your choice

8. Re-run and verify both keywords are now intercepted

## Test it

The blocked keyword returns the refusal message with no model call in the trace, while normal requests still work — and your added keyword is blocked too.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
