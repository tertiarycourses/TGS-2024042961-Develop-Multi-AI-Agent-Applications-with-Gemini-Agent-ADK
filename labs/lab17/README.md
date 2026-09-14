# Lab 17 — Ship the Agent as a Web App with Streamlit

**Topic 04:** Build an Agentic AI App with Gemini Agent ADK and Streamlit  
**Learning outcome:** LO3 — deploy a multi-agent system behind a usable chat interface.  
**Tools:** Streamlit, google-adk Runner, InMemorySessionService, asyncio

## Goal

Wrap the sequential transport agent in a Streamlit chat UI, wiring the async ADK Runner and persisting the session across Streamlit re-runs so the conversation survives.

## What you'll build

lab17 — a browser chat application backed by the multi-agent transport workflow.

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
uv run adk run lab17     # terminal chat
uv run adk web              # browser IDE, then pick lab17 at http://localhost:8000
```

## Step-by-step

1. Read how the ADK session service is stored in st.session_state

   ```bash
   cat lab17/app.py
   ```

2. The async Runner is driven by asyncio.run in the handler

3. Launch the Streamlit application

   ```bash
   uv run streamlit run lab17/app.py
   ```

4. Open the app in the browser and submit a journey

   ```bash
   From Tampines to Orchard Road
   ```

5. Send a follow-up question and confirm the conversation history is retained

   ```bash
   What if I cycle instead?
   ```

6. Refresh the browser and observe what happens to the session

7. Change the page title and icon in st.set_page_config and reload

8. Add a sidebar Clear chat button that resets st.session_state.messages

## Test it

The Streamlit app answers a journey query, retains history across follow-up turns, and your Clear chat button empties the conversation without restarting the server.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
