# Lab 14 — Build the Agentic RAG Agent — Retrieval as a Tool

**Topic 03:** Build Agentic AI RAG in Gemini ADK  
**Learning outcome:** LO4 / LO3 — wrap retrieval as a tool so the agent grounds its answers in your documents.  
**Tools:** google-adk, ChromaDB, similarity search, Gemini 3.8 Flash

## Goal

Complete the RAG loop: expose the vector search as an ADK tool, let the agent decide when to retrieve, and require it to cite the source document and page.

## What you'll build

lab14 — a grounded question-answering agent over the air-fryer manuals with citations.

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
uv run adk run lab14     # terminal chat
uv run adk web              # browser IDE, then pick lab14 at http://localhost:8000
```

## Step-by-step

1. Read the retrieval tool and how the query is embedded

   ```bash
   cat lab14/agent.py
   ```

2. Answers must come only from retrieved context

3. Run the RAG agent

   ```bash
   uv run adk run lab14
   ```

4. Ask a question answerable from the product manual

   ```bash
   What temperature should I use to air fry chicken wings?
   ```

5. Ask a question answerable only from the warranty document

   ```bash
   How long is the warranty period and what does it exclude?
   ```

6. Ask a question the documents do not cover and confirm the agent declines rather than invents

   ```bash
   What is the share price of the manufacturer?
   ```

7. In adk web, inspect the retrieval function_response to see the chunks that were retrieved

   ```bash
   uv run adk web
   ```

8. Increase the number of retrieved chunks (n_results) and re-run the same questions

## Test it

Both document questions are answered with the correct source and page cited, the out-of-scope question is refused rather than hallucinated, and you can see the retrieved chunks.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
