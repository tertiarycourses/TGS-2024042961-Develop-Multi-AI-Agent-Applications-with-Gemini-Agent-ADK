# Lab 7 — Multi-Agent Handoff — A Blog Content Production Team

**Topic 02:** Build A Multi Agent App with Gemini ADK  
**Learning outcome:** LO3 — implement agent-to-agent delegation with sub_agents.  
**Tools:** google-adk, sub_agents, google_search, Gemini 3.8 Flash

## Goal

Build a realistic editorial team: a managing editor hands off to a researcher, who gathers current facts with web search and then hands off to a writer who drafts the post. Every handoff is driven by the description field — the core ADK delegation pattern.

## What you'll build

lab07 — a three-stage content pipeline that turns a topic request into a publish-ready, fact-grounded blog post.

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
uv run adk run lab07     # terminal chat
uv run adk web              # browser IDE, then pick lab07 at http://localhost:8000
```

## Step-by-step

1. Read the three agents and the sub_agents chain

   ```bash
   cat lab07/agent.py
   ```

2. The description field is what drives the parent's handoff decision

3. Run the agent in the browser IDE

   ```bash
   uv run adk web
   ```

4. Select lab07 and commission a post

   ```bash
   Write a blog post about AI adoption in Singapore SMEs
   ```

5. In the Events tab, find the transfer_to_agent call into researcher_agent

6. Confirm the researcher's google_search calls, then the transfer into writer_agent

7. Check the finished post cites only facts that appear in the research brief

8. Weaken the writer_agent description to one vague word, re-run and observe the handoff become unreliable, then restore it

## Test it

One topic request produces a research brief followed by a cited blog post, and the Events tab shows two transfer_to_agent calls in order.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
