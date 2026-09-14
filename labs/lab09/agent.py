"""Lab 09 — Sequential Workflow: A Travel Planner Pipeline.

A realistic trip-planning assistant. Three specialists run in a FIXED order,
each writing its result into session state for the next one to read:

    destination_researcher  ->  itinerary_planner  ->  budget_analyst

Pattern: SequentialAgent (https://adk.dev/workflows/collaboration/).

The key contrast with lab07: there, the *model* decided each handoff. Here the
ORDER IS GUARANTEED BY CODE. Use SequentialAgent whenever a stage genuinely
cannot run before the previous one has finished — you never want the budget
computed before the itinerary exists.

`output_key` writes each agent's final text into session state, and the next
agent reads it back through the {curly_brace} placeholders in its instruction.
"""

from pathlib import Path
from dotenv import load_dotenv

# Load .env from the labs/ root (one .env for all agents)
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

MODEL = "gemini-3.8-flash"


# ---------- STAGE 1: research the destination ----------

destination_researcher = LlmAgent(
    model=MODEL,
    name="destination_researcher",
    description="Researches a destination's attractions, seasonality and travel basics.",
    instruction="""You are a travel research analyst.

The traveller will name a destination and trip length. Use the google_search
tool to gather current, factual information:

- The 5-6 highest-value attractions, with the typical visit duration of each
- The weather and seasonality for the travel period
- Local transport options and roughly what they cost
- One practical warning (a closure, a scam, a permit that must be booked ahead)

Output a structured "DESTINATION BRIEF" in Markdown. Report facts only —
do not build a day-by-day plan; that is the next agent's job.

If the traveller has not given a destination and trip length, ask for both
before researching.
""",
    tools=[google_search],
    output_key="destination_brief",
)


# ---------- STAGE 2: build the itinerary from that research ----------

itinerary_planner = LlmAgent(
    model=MODEL,
    name="itinerary_planner",
    description="Turns a destination brief into a realistic day-by-day itinerary.",
    instruction="""You are an itinerary planner.

Here is the research brief prepared for this trip:

{destination_brief}

Build a day-by-day itinerary from it. For each day give:
- A morning, afternoon and evening block
- Travel time between locations
- One recommended meal stop

Rules:
- Group attractions that are geographically close on the same day.
- Do not schedule more than three major attractions in one day.
- Use ONLY attractions named in the brief above.

Output as "ITINERARY" in Markdown, with one sub-heading per day.
""",
    output_key="itinerary",
)


# ---------- STAGE 3: cost the finished itinerary ----------

budget_analyst = LlmAgent(
    model=MODEL,
    name="budget_analyst",
    description="Produces a per-traveller cost breakdown for a finished itinerary.",
    instruction="""You are a travel budget analyst.

Here is the planned itinerary:

{itinerary}

Produce a realistic cost estimate per traveller in SGD, broken down into:
- Accommodation (per night x nights)
- Attractions and entrance fees
- Local transport
- Food (per day estimate)

Then give a TOTAL, plus a budget and a comfortable variant of that total.

End with two concrete suggestions for cutting the cost without removing a
major attraction. Output as "BUDGET" in Markdown with a costs table.
""",
    output_key="budget",
)


# ---------- THE PIPELINE ----------
# SequentialAgent guarantees research -> itinerary -> budget, in that order.

travel_planning_pipeline = SequentialAgent(
    name="travel_planning_pipeline",
    description=(
        "Runs the full trip-planning workflow: research the destination, build "
        "the itinerary, then cost it."
    ),
    sub_agents=[destination_researcher, itinerary_planner, budget_analyst],
)

root_agent = travel_planning_pipeline
