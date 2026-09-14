# Lab 12 — Connect External Tools with MCP — StreamableHTTP and SSE

**Topic 02:** Build A Multi Agent App with Gemini ADK  
**Learning outcome:** LO3 / LO2 — integrate third-party tools through the Model Context Protocol.  
**Tools:** google-adk, McpToolset, StreamableHTTPConnectionParams, SseConnectionParams, n8n MCP server

## Goal

Connect an ADK agent to a remote MCP server so it can use tools it does not own, using both the StreamableHTTP and SSE transports.

## What you'll build

lab12 — agent.py (StreamableHTTP) and agent_sse.py (SSE), whose toolset is discovered at runtime from an MCP server.

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
uv run adk run lab12     # terminal chat
uv run adk web              # browser IDE, then pick lab12 at http://localhost:8000
```

## Agent scripts in this lab

- `agent.py` — the default agent loaded by `adk run lab12`
- `agent_sse.py`

Open `uv run adk web` and select the script you want to run.

## Step-by-step

1. Read how McpToolset discovers tools from the server URL

   ```bash
   cat lab12/agent.py
   ```

2. Run the StreamableHTTP MCP agent and read the printed tool list

   ```bash
   uv run python lab12/agent.py
   ```

3. Send a request that exercises one of the discovered tools

4. Compare the SSE variant and note that only the connection params differ

   ```bash
   cat lab12/agent.py
   ```

5. Explain when SSE is preferred over StreamableHTTP

6. Point the MCP_SERVER_URL at a different MCP server and re-run

7. Confirm the agent's available tools change without any change to the agent code

## Test it

The agent prints the tools discovered from the MCP server and successfully invokes one; changing the server URL changes the toolset with no code edit.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
