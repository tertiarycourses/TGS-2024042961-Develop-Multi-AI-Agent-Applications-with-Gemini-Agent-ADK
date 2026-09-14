# Lab 1 — Set Up the Gemini ADK Environment and Get an API Key

**Topic 01:** Overview of Agentic AI in Gemini ADK  
**Learning outcome:** LO1 / LO2 — establish a working Gemini ADK development environment.  
**Tools:** Google AI Studio, uv, Python 3.13, google-adk, python-dotenv, gemini-3.8-flash

## Goal

Install the Agent Development Kit toolchain with uv, obtain a free Google AI Studio API key, store it safely in a .env file, and verify the Gemini model the whole course runs on. Every later lab depends on this setup working.

## What you'll build

A working Python 3.13 project with google-adk installed, a validated GOOGLE_API_KEY and a confirmed gemini-3.8-flash connection.

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
uv run adk run lab01     # terminal chat
uv run adk web              # browser IDE, then pick lab01 at http://localhost:8000
```

## Step-by-step

1. Clone the course lab repository from GitHub

   ```bash
   git clone https://github.com/tertiarycourses/TGS-2024042961-Develop-Multi-AI-Agent-Applications-with-Gemini-Agent-ADK.git
   ```

2. Change into the labs folder

   ```bash
   cd TGS-2024042961-Develop-Multi-AI-Agent-Applications-with-Gemini-Agent-ADK/labs
   ```

3. Install all dependencies with uv (creates the .venv automatically)

   ```bash
   uv sync
   ```

4. Open Google AI Studio and sign in with your Google account, then click Get API key → Create API key

5. Create a .env file in the labs folder and paste your key

   ```bash
   cat > .env <<'EOF'
   GOOGLE_GENAI_USE_VERTEXAI=0
   GOOGLE_API_KEY=your-google-api-key
   OPENWEATHER_API_KEY=your-openweather-key
   TAVILY_API_KEY=your-tavily-key
   EOF
   ```

6. Confirm the ADK command-line tool is on the path

   ```bash
   uv run adk --help
   ```

7. Run the setup verifier — it checks Python, google-adk, the key and a live model call

   ```bash
   uv run python lab01/verify_setup.py
   ```

8. Note the MODEL constant every lab uses, and why the ID is declared once per file

   ```bash
   gemini-3.8-flash
   ```

9. Confirm .env is git-ignored so your API key is never committed

   ```bash
   git check-ignore -v .env
   ```

## Test it

uv run python lab01/verify_setup.py reports PASS on every check, including a live gemini-3.8-flash response, and git check-ignore confirms .env is excluded from commits.

---

*Develop Multi AI Agent Applications with Gemini Agent ADK (TGS-2024042961) v1.4 — © 2026 Tertiary Infotech Academy Pte Ltd*
