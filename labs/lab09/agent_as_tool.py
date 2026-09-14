"""Lab 09d — Agent-as-a-Tool: A Report Writer with Specialist Services.

A business analyst agent that CALLS two specialists the way it would call any
other tool — a summariser and a translator — and keeps control throughout.

Pattern: AgentTool (https://adk.dev/workflows/collaboration/).

This is the distinction that most often trips people up:

  sub_agents=[x]              -> HANDOFF. Control TRANSFERS to x. x now owns
                                 the conversation and replies to the user
                                 directly. The parent is done.

  tools=[AgentTool(agent=x)]  -> CALL. x runs, RETURNS ITS RESULT to the
                                 parent, and the parent carries on composing
                                 the final answer. Control never leaves.

Use AgentTool whenever the specialist produces an INTERMEDIATE result the
parent still needs to work with — exactly like this report writer, which needs
the summary and the translation in order to assemble one document.

Run with:  uv run adk web   (then pick lab09 and select this agent)
"""

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

MODEL = "gemini-3.8-flash"


# ---------- SPECIALIST 1: summarisation as a service ----------

summariser_agent = LlmAgent(
    model=MODEL,
    name="summariser_agent",
    description=(
        "Condenses a long passage of text into a brief executive summary. "
        "Pass the full text to be summarised as the request."
    ),
    instruction="""You are an executive summariser.

Condense the text you are given into at most three sentences that a busy
executive could read in twenty seconds. Preserve every figure and date.
Return the summary only — no preamble, no commentary.
""",
)


# ---------- SPECIALIST 2: translation as a service ----------

translator_agent = LlmAgent(
    model=MODEL,
    name="translator_agent",
    description=(
        "Translates business text into Simplified Chinese. Pass the text to "
        "be translated as the request."
    ),
    instruction="""You are a professional business translator.

Translate the text you are given into Simplified Chinese, using natural
business register rather than a literal word-for-word rendering. Keep all
figures, dates and company names unchanged.
Return the translation only.
""",
)


# ---------- THE ANALYST: calls both, keeps control ----------

root_agent = LlmAgent(
    model=MODEL,
    name="bilingual_report_writer",
    description="Produces a bilingual executive report from raw business notes.",
    instruction="""You are a business analyst who produces bilingual reports for
a regional leadership team.

When the user gives you raw notes, a transcript or a long report:

1. Call summariser_agent with the full text to obtain an executive summary.
2. Call translator_agent with THAT SUMMARY to obtain the Chinese version.
3. Assemble both into one document:

   ## Executive Summary
   (the English summary)

   ## 执行摘要
   (the Chinese translation)

   ## Recommended Actions
   (2-3 concrete actions you infer from the material)

The Recommended Actions are your own analysis — the specialists do not supply
them. Note that you remain in control the whole time: each specialist returns
its result to you rather than replying to the user directly.
""",
    tools=[
        AgentTool(agent=summariser_agent),
        AgentTool(agent=translator_agent),
    ],
)
