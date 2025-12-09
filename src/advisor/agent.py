from google.adk.agents.llm_agent import Agent
from pathlib import Path
from advisor.tools import get_service_offerings
from advisor.tools import get_professional_experience
from helper import read_prompt


agent_name = "advisor"
root_agent = Agent(
    name=agent_name,
    model="gemini-2.5-flash",
    description=read_prompt(agent_name, "purpose"),
    instruction=read_prompt(agent_name, "system"),
    tools=[get_service_offerings, get_professional_experience],
)
