# Develop Multi AI Agent Applications with Gemini Agent ADK — Hands-On Labs

**Course Code:** TGS-2024042961  ·  **18 labs across 4 topics**  ·  **v1.4**

Every lab lives in its own self-contained folder — `lab01` … `lab18` — holding that lab's
agent script, any data files it needs, and a `README.md` lab sheet with the full
step-by-step. Detailed walkthroughs are also in the **Learner Guide**
(`LG-*.md` at the repo root, or the DOCX/PDF in `courseware/`).

## Setup (once)

```bash
cd labs
uv sync                 # installs google-adk and every dependency
cp .env.example .env    # then paste your GOOGLE_API_KEY into .env
```

Every agent in this course runs on **`gemini-3.8-flash`**.

## Running a lab

```bash
uv run adk run lab02    # terminal chat with that lab's agent
uv run adk web          # browser IDE at http://localhost:8000 — pick any lab
```

## The labs

| # | Folder | Lab | Topic |
|---|---|---|---|
| 1 | [`lab01`](lab01/) | [Set Up the Gemini ADK Environment and Get an API Key](lab01/README.md) | 1 |
| 2 | [`lab02`](lab02/) | [Build Your First ADK Agent — A Retail Banking Assistant](lab02/README.md) | 1 |
| 3 | [`lab03`](lab03/) | [Give an Agent Tools — Live Weather and Web Search](lab03/README.md) | 1 |
| 4 | [`lab04`](lab04/) | [Swap the Model — Running an ADK Agent on a Non-Gemini LLM](lab04/README.md) | 1 |
| 5 | [`lab05`](lab05/) | [Give an Agent Memory — Sessions, State and the Runner](lab05/README.md) | 2 |
| 6 | [`lab06`](lab06/) | [Inspect the Agent Loop — Events, Tool Calls and Final Responses](lab06/README.md) | 2 |
| 7 | [`lab07`](lab07/) | [Multi-Agent Handoff — A Blog Content Production Team](lab07/README.md) | 2 |
| 8 | [`lab08`](lab08/) | [Coordinator / Dispatcher — A Customer Support Desk](lab08/README.md) | 2 |
| 9 | [`lab09`](lab09/) | [Workflow Agents — Sequential, Parallel, Loop and Agent-as-a-Tool](lab09/README.md) | 2 |
| 10 | [`lab10`](lab10/) | [Add a Guardrail — Blocking Unsafe Requests with a Callback](lab10/README.md) | 2 |
| 11 | [`lab11`](lab11/) | [Structured Output — Forcing Valid JSON with Pydantic](lab11/README.md) | 2 |
| 12 | [`lab12`](lab12/) | [Connect External Tools with MCP — StreamableHTTP and SSE](lab12/README.md) | 2 |
| 13 | [`lab13`](lab13/) | [Load, Split and Embed Documents into a Vector Store](lab13/README.md) | 3 |
| 14 | [`lab14`](lab14/) | [Build the Agentic RAG Agent — Retrieval as a Tool](lab14/README.md) | 3 |
| 15 | [`lab15`](lab15/) | [Evaluate RAG Performance — Retrieval Quality and Groundedness](lab15/README.md) | 3 |
| 16 | [`lab16`](lab16/) | [Declarative Agents — Configuring a Multi-Agent System in YAML](lab16/README.md) | 4 |
| 17 | [`lab17`](lab17/) | [Ship the Agent as a Web App with Streamlit](lab17/README.md) | 4 |
| 18 | [`lab18`](lab18/) | [Capstone — Build Your Own Multi-Agent Application](lab18/README.md) | 4 |

## Topics

| Topic | Title | Labs |
|---|---|---|
| 01 | Overview of Agentic AI in Gemini ADK | 1–4 |
| 02 | Build A Multi Agent App with Gemini ADK | 5–12 |
| 03 | Build Agentic AI RAG in Gemini ADK | 13–15 |
| 04 | Build an Agentic AI App with Gemini Agent ADK and Streamlit | 16–18 |

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
