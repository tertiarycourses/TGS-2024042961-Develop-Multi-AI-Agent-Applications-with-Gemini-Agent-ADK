# WSQ — Develop Multi AI Agent Applications with Gemini Agent ADK

**Course Code:** TGS-2024042961
**Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)
**Duration:** 2 days · 16 training hours

Courseware and hands-on lab repository for the WSQ course *Develop Multi AI Agent Applications
with Gemini Agent ADK*, built on Google's open-source [Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
and the Gemini model family.

---

## Learning Outcomes

| | Outcome |
|---|---|
| **LO1** | Analyze the range of LLM applications using Generative AI (GAI) and identify their industrial use cases |
| **LO2** | Establish Google Gemini GAI designs and assess improvements on engineering processes |
| **LO3** | Develop LLM applications and assess its feasibility |
| **LO4** | Evaluate the performance effectiveness of Retrieval Augmented Generation (RAG) |

---

## Course Topics

| Topic | Title | Labs |
|---|---|---|
| 1 | Overview of Agentic AI in Gemini ADK | 1–4 |
| 2 | Build A Multi Agent App with Gemini ADK | 5–12 |
| 3 | Build Agentic AI RAG in Gemini ADK | 13–15 |
| 4 | Build an Agentic AI App with Gemini Agent ADK and Streamlit | 16–18 |

---

## Quick Start

**Prerequisites:** Python 3.13+, [uv](https://docs.astral.sh/uv/), and a free Gemini API key from
[Google AI Studio](https://aistudio.google.com).

```bash
git clone https://github.com/tertiarycourses/TGS-2024042961-Develop-Multi-AI-Agent-Applications-with-Gemini-Agent-ADK.git
cd TGS-2024042961-Develop-Multi-AI-Agent-Applications-with-Gemini-Agent-ADK/labs
uv sync
```

Create a `.env` file in the `labs/` folder:

```env
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your-google-api-key
OPENWEATHER_API_KEY=your-openweather-key   # optional, tool labs
TAVILY_API_KEY=your-tavily-key             # optional, search labs
```

> **Never commit your `.env` file or API keys.** It is git-ignored in this repository.

Run any agent:

```bash
uv run adk run <agent_folder>   # terminal chat
uv run adk web                  # browser IDE at http://localhost:8000
```

---

## Labs

| # | Lab | Agent folder | Topic |
|---|---|---|---|
| 1 | Set Up the Gemini ADK Environment and Get an API Key | `lab01` | 1 |
| 2 | Build Your First ADK Agent — A Retail Banking Assistant | `lab02` | 1 |
| 3 | Give an Agent Tools — Live Weather and Web Search | `lab03` | 1 |
| 4 | Swap the Model — Running an ADK Agent on a Non-Gemini LLM | `lab04` | 1 |
| 5 | Give an Agent Memory — Sessions, State and the Runner | `lab05` | 2 |
| 6 | Inspect the Agent Loop — Events, Tool Calls and Final Responses | `lab06` | 2 |
| 7 | Multi-Agent Handoff — Joke Generator to Translator | `lab07` | 2 |
| 8 | Hierarchical Multi-Agent System — The Tutor Agent | `lab08` | 2 |
| 9 | Sequential Workflow Agent — Singapore Transport Route Planner | `lab09` | 2 |
| 10 | Add a Guardrail — Blocking Unsafe Requests with a Callback | `lab10` | 2 |
| 11 | Structured Output — Forcing Valid JSON with Pydantic | `lab11` | 2 |
| 12 | Connect External Tools with MCP — StreamableHTTP and SSE | `lab12` | 2 |
| 13 | Load, Split and Embed Documents into a Vector Store | `lab13` | 3 |
| 14 | Build the Agentic RAG Agent — Retrieval as a Tool | `lab14` | 3 |
| 15 | Evaluate RAG Performance — Retrieval Quality and Groundedness | `lab15` | 3 |
| 16 | Declarative Agents — Configuring a Multi-Agent System in YAML | `lab16` | 4 |
| 17 | Ship the Agent as a Web App with Streamlit | `lab17` | 4 |
| 18 | Capstone — Design, Build and Assess Your Own Multi-Agent Application | `lab18` | 4 |

Every lab is a **self-contained folder** holding its own agent script, data files and a
`README.md` lab sheet. See [labs/LABS.md](labs/LABS.md) for the full index.

---

## Core ADK Patterns

**Define an agent**

```python
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer clearly and concisely.',
)
```

**Add a tool** — the docstring and type hints are the contract the model reads.

```python
def get_weather(city: str) -> dict:
    """Retrieves the current weather for a specified city.

    Args:
        city (str): The name of the city.

    Returns:
        dict: status and result or error msg.
    """
    return {"status": "success", "report": "..."}

agent = Agent(..., tools=[get_weather])
```

**Multi-agent handoff**

```python
root_agent = Agent(
    name='root_agent',
    sub_agents=[math_tutor_agent, physics_tutor_agent, history_tutor_agent],
    instruction='Route each question to the right specialist.',
)
```

**Sequential workflow**

```python
from google.adk.agents import SequentialAgent

workflow = SequentialAgent(
    name='workflow_agent',
    sub_agents=[input_agent, research_agent, report_agent],
)
```

**Guardrail** — return `None` to allow, an `LlmResponse` to block.

```python
def block_keyword_guardrail(callback_context, llm_request):
    if "BLOCK" in last_user_message.upper():
        return LlmResponse(content=types.Content(
            role="model", parts=[types.Part(text="I cannot process this request.")]))
    return None

agent = Agent(..., before_model_callback=block_keyword_guardrail)
```

**Structured output** — note an agent with `output_schema` cannot also use tools.

```python
from pydantic import BaseModel

class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    cooking_time: int

agent = Agent(..., output_schema=Recipe)
```

---

## Courseware

| Artifact | File |
|---|---|
| Trainer Slides | `courseware/Develop Multi AI Agent Applications with Gemini Agent ADK-v1.4.pptx` |
| Learner Slides (PDF) | `courseware/Develop Multi AI Agent Applications with Gemini Agent ADK-v1.4.pdf` |
| Lesson Plan | `courseware/LP-Develop Multi AI Agent Applications with Gemini Agent ADK.docx` |
| Learner Guide | `courseware/LG-Develop Multi AI Agent Applications with Gemini Agent ADK.docx` |
| Learner Guide (Markdown) | `LG-Develop Multi AI Agent Applications with Gemini Agent ADK.md` |

The **Learner Guide** carries the full step-by-step instructions for all 18 labs, plus reference
sections on core ADK patterns, evaluating a RAG pipeline, and assessing the feasibility of an
agent application.

The **Trainer Slides** (v1.4, 162 slides) teach each lab as a four-part unit — briefing →
process map → procedure with the actual commands → verification with troubleshooting — alongside
comparison matrices, decision maps, worked code examples and native charts. Slide transitions are
deliberately restrained (content fades, section dividers push), with click-through reveals on the
process maps so a stage can be discussed before the next appears.

> The assessment set is confidential and is **not** published in this repository.

---

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google AI Studio](https://aistudio.google.com) — free Gemini API keys
- [Course page](https://www.tertiarycourses.com.sg/wsq-develop-multi-ai-agent-applications-with-gemini-agent-adk.html)
- [LMS / TMS](https://lms-tms.tertiaryinfotech.com)

## Support

**Tertiary Infotech Academy Pte Ltd** · UEN 201200696W
Email: enquiry@tertiaryinfotech.com · Tel: +65 6100 0613 · [tertiarycourses.com.sg](https://www.tertiarycourses.com.sg)

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
