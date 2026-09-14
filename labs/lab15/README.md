# Lab 15 — Evaluate RAG Performance — Retrieval Quality and Groundedness

**Topic 03:** Build Agentic AI RAG in Gemini ADK  
**Learning outcome:** LO4 — evaluate the performance effectiveness of a RAG implementation.  
**Tools:** lab15, ChromaDB, similarity search vs MMR

## Goal

Build a small evaluation set and score your RAG agent on retrieval hit rate, groundedness, answer relevance and latency, then tune one parameter and measure the improvement.

## What you'll build

A completed RAG evaluation table with a before-and-after comparison for one tuned parameter.

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
uv run adk run lab15     # terminal chat
uv run adk web              # browser IDE, then pick lab15 at http://localhost:8000
```

## Step-by-step

1. Write eight test questions: six answerable from the PDFs, two deliberately out of scope

2. For each question record whether the correct chunk was retrieved (retrieval hit)

3. Record whether every claim is grounded in the retrieved text

4. Record whether the answer actually addresses the question (relevance) and its response time

5. Compute the hit rate, groundedness rate and mean latency across the eight questions

6. Tune one parameter — chunk size, n_results, or switch similarity search to MMR

7. Re-run the same eight questions and recompute all three metrics

8. State which parameter change you would keep and justify it with your numbers

## Test it

A completed evaluation table with before-and-after figures for retrieval hit rate, groundedness and latency, plus a written, evidence-based tuning recommendation.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
