from pathlib import Path
from dotenv import load_dotenv

# Load .env from the labs/ root (one .env for all agents)
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from pydantic import BaseModel
from google.adk.agents import Agent


# --- Pydantic Model for Structured Output ---
class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    cooking_time: int  # in minutes
    servings: int
    instructions: list[str]


# --- Agent with Structured Output ---
#
# MODEL CHOICE MATTERS HERE — DO NOT BULK-SWAP THIS LINE.
#
# Structured output is a MODEL CAPABILITY, not just a config flag. On a "lite"
# tier (e.g. gemini-3.1-flash-lite) this exact agent returns an empty JSON
# object and exits 0 — no error, no warning, no traceback:
#
#     [recipe_agent]: {
#     }
#
# That silent failure is far worse than a crash, because the lab looks like it
# ran. Use a full Flash tier or better, and if you change this model, actually
# run the lab and confirm all five fields come back populated and correctly
# typed before committing.
root_agent = Agent(
    name="recipe_agent",
    model="gemini-3.8-flash",
    description="An agent that creates detailed recipes in structured format.",
    instruction=(
        "You are an agent for creating recipes. You will be given the name of a food and your job "
        "is to output that as an actual detailed recipe. The cooking time should be in minutes. "
        "Always respond with a valid JSON object matching this schema:\n"
        "{\n"
        '  "title": "Recipe name",\n'
        '  "ingredients": ["ingredient 1", "ingredient 2", ...],\n'
        '  "cooking_time": number (in minutes),\n'
        '  "servings": number,\n'
        '  "instructions": ["step 1", "step 2", ...]\n'
        "}"
    ),
    output_schema=Recipe,
)
