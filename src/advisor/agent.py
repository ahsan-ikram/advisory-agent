from google.adk.agents.llm_agent import Agent

from helper import read_prompt


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction= read_prompt("system"),
)
