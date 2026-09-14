# Lab 16 — Declarative Agents — Configuring a Multi-Agent System in YAML

**Topic 04:** Build an Agentic AI App with Gemini Agent ADK and Streamlit  
**Learning outcome:** LO2 / LO3 — separate agent configuration from code to improve maintainability.  
**Tools:** google-adk YAML config, LlmAgent, Gemini 3.8 Flash

## Goal

Define a five-specialist transport assistant entirely in YAML config files, with no Python agent code, and assess what this buys you for maintainability and governance.

## What you'll build

lab16 — a root agent with MRT, bus, taxi, bike and walk specialists, all declared in YAML.

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
uv run adk run lab16     # terminal chat
uv run adk web              # browser IDE, then pick lab16 at http://localhost:8000
```

## Step-by-step

1. List the YAML files and note one file per agent

   ```bash
   ls lab16/
   ```

2. Read the root agent config and its sub_agents config_path list

   ```bash
   cat lab16/root_agent.yaml
   ```

3. Read one specialist config and compare its fields to the Python Agent(...) arguments

   ```bash
   cat lab16/mrt_agent.yaml
   ```

4. Run the YAML-configured agent

   ```bash
   uv run adk web
   ```

5. Ask an MRT question and confirm it routes to mrt_agent

   ```bash
   What is the fastest MRT route from Bugis to Woodlands?
   ```

6. Ask a cycling question and confirm it routes to bike_agent

7. Add a sixth specialist by creating a new YAML file and referencing it in root_agent.yaml

8. Re-run and confirm the new specialist is routed to without touching any Python file

## Test it

All five specialists route correctly, and your sixth agent works after editing YAML only — no Python file was modified.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
