"""Lab 09c — Loop Workflow: A Writer / Critic Refinement Cycle.

A realistic copy-editing cycle. A writer drafts marketing copy, a critic reviews
it against explicit quality criteria, and the pair iterate until the critic is
satisfied — or until the iteration cap is reached.

Pattern: LoopAgent with an escape hatch
(https://adk.dev/workflows/collaboration/).

Two things make a loop safe, and both matter in production:

  1. `max_iterations` — a hard ceiling so the loop always terminates and the
     token bill cannot run away.
  2. An explicit exit signal — the critic calls the `approve_copy` tool, which
     sets `tool_context.actions.escalate = True` to break the loop early once
     the work is genuinely good enough.

Without the escape hatch you always pay for every iteration, even when the
first draft was already fine.

Run with:  uv run adk web   (then pick lab09 and select this agent)
"""

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from google.adk.agents import LlmAgent, LoopAgent, SequentialAgent
from google.adk.tools.tool_context import ToolContext

MODEL = "gemini-3.8-flash"


# ---------- THE EXIT SIGNAL ----------

def approve_copy(reason: str, tool_context: ToolContext) -> dict:
    """Approve the current draft and stop the revision loop.

    Call this ONLY when the draft meets every quality criterion.

    Args:
        reason: A short statement of why the draft now passes.

    Returns:
        A confirmation that the loop has been stopped.
    """
    # This is what actually breaks the LoopAgent out early.
    tool_context.actions.escalate = True
    return dict(status="approved", reason=reason)


# ---------- THE WRITER ----------

writer_agent = LlmAgent(
    model=MODEL,
    name="writer_agent",
    description="Drafts and revises marketing copy for a product landing page.",
    instruction="""You are a marketing copywriter.

If there is no draft yet, write the first version of the landing-page copy for
the product the user described: a headline, a sub-headline, three benefit
bullets and a call to action.

If a previous draft and critique exist below, write an IMPROVED version that
addresses every point the critic raised. Do not defend the old draft — revise it.

PREVIOUS DRAFT:
{draft?}

CRITIQUE TO ADDRESS:
{critique?}

Output the full revised copy only, with no commentary about what you changed.
""",
    output_key="draft",
)


# ---------- THE CRITIC ----------

critic_agent = LlmAgent(
    model=MODEL,
    name="critic_agent",
    description="Reviews marketing copy and either demands revisions or approves it.",
    instruction="""You are a demanding copy chief reviewing this draft:

{draft}

Judge it against four criteria:
1. The headline states a concrete benefit, not a vague claim.
2. Every bullet is specific — no filler words like "powerful" or "seamless"
   standing alone without evidence.
3. The call to action names one clear next step.
4. No sentence exceeds 25 words.

If the draft FAILS any criterion: list each failure as a numbered, specific,
actionable instruction. Do not rewrite the copy yourself. Do not approve.

If the draft PASSES all four: call the approve_copy tool with your reason.
Be genuinely strict on the first draft — approving too early defeats the loop.
""",
    tools=[approve_copy],
    output_key="critique",
)


# ---------- THE LOOP ----------

refinement_loop = LoopAgent(
    name="refinement_loop",
    description="Iterates writer then critic until the copy is approved.",
    sub_agents=[writer_agent, critic_agent],
    max_iterations=3,   # hard ceiling: the loop can never run away
)


# ---------- FINAL PACKAGING ----------

finaliser_agent = LlmAgent(
    model=MODEL,
    name="finaliser_agent",
    description="Presents the approved copy with a summary of the revision cycle.",
    instruction="""The revision loop has finished. Present the final copy:

{draft}

Then add a short "REVISION NOTES" section describing what the last critique
asked for, so the client can see how the copy improved.
""",
)

root_agent = SequentialAgent(
    name="copy_refinement_system",
    description=(
        "Drafts marketing copy and refines it through a writer/critic loop "
        "until it passes review."
    ),
    sub_agents=[refinement_loop, finaliser_agent],
)
