"""Lab 09b — Parallel Workflow: A Market Research Desk.

Three analysts research three INDEPENDENT angles of the same company at the
same time, then a synthesiser merges their findings into one investment brief.

Pattern: ParallelAgent + a synthesis step
(https://adk.dev/workflows/collaboration/).

Why parallel and not sequential? These three research tasks do not depend on
each other — the competitor analysis does not need the financial summary to
start. Running them concurrently cuts wall-clock latency to roughly the slowest
branch instead of the sum of all three.

The rule to remember: use SequentialAgent when stage N needs stage N-1's
output; use ParallelAgent when the branches are genuinely independent.

Run with:  uv run adk web   (then pick lab09 and select this agent)
"""

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

MODEL = "gemini-3.8-flash"


# ---------- THE THREE INDEPENDENT BRANCHES ----------

financial_analyst = LlmAgent(
    model=MODEL,
    name="financial_analyst",
    description="Researches a company's financial performance.",
    instruction="""You are a financial analyst.

For the company named by the user, use google_search to find:
- The most recent reported revenue and profit, with the period they cover
- Revenue growth versus the previous year
- Any recent guidance, profit warning or major write-down

Report only figures you actually found, each with its source and date.
If a figure is unavailable, say so explicitly rather than estimating.

Output under the heading "FINANCIALS", maximum 200 words.
""",
    tools=[google_search],
    output_key="financials",
)

competitor_analyst = LlmAgent(
    model=MODEL,
    name="competitor_analyst",
    description="Researches a company's competitive position.",
    instruction="""You are a competitive intelligence analyst.

For the company named by the user, use google_search to find:
- Its three closest competitors
- Its main differentiator versus each
- Any market share figure you can source
- One recent competitive threat (a launch, a price cut, a new entrant)

Output under the heading "COMPETITIVE LANDSCAPE", maximum 200 words.
Cite a source for every claim.
""",
    tools=[google_search],
    output_key="competition",
)

sentiment_analyst = LlmAgent(
    model=MODEL,
    name="sentiment_analyst",
    description="Researches public and press sentiment about a company.",
    instruction="""You are a market sentiment analyst.

For the company named by the user, use google_search to find:
- The tone of coverage over the past six months (positive, mixed, negative)
- Two specific recent news events that moved perception
- Any notable analyst upgrade or downgrade

Output under the heading "SENTIMENT", maximum 200 words.
Distinguish clearly between reported fact and opinion.
""",
    tools=[google_search],
    output_key="sentiment",
)


# ---------- FAN OUT: all three run concurrently ----------

research_fan_out = ParallelAgent(
    name="research_fan_out",
    description="Runs financial, competitive and sentiment research concurrently.",
    sub_agents=[financial_analyst, competitor_analyst, sentiment_analyst],
)


# ---------- FAN IN: merge the three branches ----------

synthesis_agent = LlmAgent(
    model=MODEL,
    name="synthesis_agent",
    description="Merges the three research branches into one investment brief.",
    instruction="""You are the head of research. Three analysts have reported.

FINANCIALS:
{financials}

COMPETITIVE LANDSCAPE:
{competition}

SENTIMENT:
{sentiment}

Write a single INVESTMENT BRIEF that:
1. Opens with a two-sentence summary of the company's position.
2. Highlights where the three reports AGREE — those are your confident findings.
3. Flags explicitly where they CONFLICT, and says which you weight more and why.
4. Lists the three biggest risks.
5. Ends with a clear recommendation: Positive, Neutral or Negative, with the
   single most important reason.

Use only what the three analysts reported. Do not add outside facts.
""",
    output_key="investment_brief",
)


# ---------- FAN OUT, THEN FAN IN ----------

root_agent = SequentialAgent(
    name="market_research_desk",
    description=(
        "Researches a company from three angles in parallel, then synthesises "
        "the findings into one investment brief."
    ),
    sub_agents=[research_fan_out, synthesis_agent],
)
