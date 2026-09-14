from pathlib import Path
from dotenv import load_dotenv

# Load .env from the labs/ root (one .env for all agents)
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from google.adk.agents import Agent

MODEL = "gemini-3.1-flash-lite"

# Sub-agent: Translates jokes into Chinese
translator_agent = Agent(
    name="translator",
    model=MODEL,
    description="Translates English text into Chinese. Use this agent when translation to Chinese is needed.",
    instruction="""You are a professional translator specializing in English to Chinese translation.

When you receive text (especially jokes), translate it into Mandarin Chinese.
Preserve the humor and meaning of the original text as much as possible.
Provide both the Chinese characters and pinyin romanization.""",
)

# Sub-agent: Generates jokes
joke_generator_agent = Agent(
    name="joke_generator",
    model=MODEL,
    description="Generates jokes. Use this agent when the user asks for jokes.",
    instruction="""You are a comedian who tells funny jokes.

When asked for a joke, generate a short, family-friendly joke.
After telling the joke in English, ALWAYS transfer to the translator agent to translate it into Chinese.
This ensures the user gets both the English and Chinese versions.""",
    sub_agents=[translator_agent],
)

# Root agent: Orchestrates the interaction
root_agent = Agent(
    name="root_agent",
    model=MODEL,
    description="Root agent that handles user requests and delegates to specialized agents.",
    instruction="""You are a friendly assistant.

When the user asks for a joke:
1. Transfer to the joke_generator agent to generate a joke
2. The joke_generator will automatically hand off to the translator for Chinese translation

For other requests, respond helpfully.""",
    sub_agents=[joke_generator_agent],
)
