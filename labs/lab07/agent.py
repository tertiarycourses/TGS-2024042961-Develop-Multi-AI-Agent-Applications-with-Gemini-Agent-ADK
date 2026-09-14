"""Lab 07 — Multi-Agent Handoff: A Content Production Team.

A realistic editorial workflow. A managing editor receives a blog brief and hands
off to a researcher, who gathers current facts and then hands off to a writer.
Each handoff is an ADK `transfer_to_agent` call driven purely by the `description`
field — the parent reads the descriptions to decide where control should go.

Pattern: sequential HANDOFF via sub_agents (agent-directed delegation).
Contrast with lab09, where SequentialAgent enforces the order in code.
"""

from pathlib import Path
from dotenv import load_dotenv

# Load .env from the labs/ root (one .env for all agents)
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from google.adk.agents import Agent
from google.adk.tools import google_search

# Gemini 3.8 Flash — engineered for autonomous agents and multi-step reasoning,
# which is exactly what a multi-agent handoff chain needs.
# See https://adk.dev/agents/models/google-gemini/
MODEL = "gemini-3.8-flash"


# ---------- STAGE 3: the writer (end of the chain) ----------

writer_agent = Agent(
    name="writer_agent",
    model=MODEL,
    description=(
        "Writes the final publish-ready blog post from a research brief. "
        "Use this agent once research notes have been gathered and the post "
        "needs to be drafted."
    ),
    instruction="""You are a senior content writer for a technology blog.

You will receive a research brief containing facts, statistics and sources.
Turn it into a publish-ready blog post:

- An attention-grabbing title
- A one-paragraph introduction that states why the topic matters now
- Three to four body sections with descriptive sub-headings
- A short conclusion with a clear takeaway for the reader

Rules:
- Use ONLY facts present in the research brief. Never invent statistics.
- Cite the source inline in brackets when you use a specific figure.
- Target roughly 400-500 words in Markdown.
""",
)


# ---------- STAGE 2: the researcher (hands off to the writer) ----------

researcher_agent = Agent(
    name="researcher_agent",
    model=MODEL,
    description=(
        "Researches a blog topic using web search and produces a factual "
        "research brief. Use this agent when a topic has been chosen but no "
        "facts have been gathered yet."
    ),
    instruction="""You are a research analyst supporting a content team.

For the topic you are given, use the google_search tool to gather:
- The 3-5 most important current facts, with figures and dates
- At least one recent development or trend from the past year
- The source (publication and URL) for every figure you report

Compile these into a clearly structured research brief under the heading
"RESEARCH BRIEF", listing each fact as a bullet with its source.

When the brief is complete, ALWAYS transfer to the writer_agent so the post
can be drafted. Do not write the blog post yourself.
""",
    tools=[google_search],
    sub_agents=[writer_agent],
)


# ---------- STAGE 1: the managing editor (entry point) ----------

root_agent = Agent(
    name="managing_editor",
    model=MODEL,
    description="Managing editor that runs a blog post from brief to finished draft.",
    instruction="""You are the managing editor of a technology blog.

When a user requests a blog post on a topic:
1. Confirm the topic and the intended audience in one short sentence.
2. Transfer to the researcher_agent to gather the facts.
3. The researcher will hand off to the writer_agent automatically, so you do
   not need to manage that second step.

If the user's topic is vague, ask ONE clarifying question before starting.
Never write the post or do the research yourself — your job is delegation.
""",
    sub_agents=[researcher_agent],
)
