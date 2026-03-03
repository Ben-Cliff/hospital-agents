import os
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai import types

# Import the root_agent from the other agent files
from src.agents.doctor.agent import root_agent as doctor_agent
from src.agents.receptionist.agent import root_agent as receptionist_agent
# TODO: Import the researcher_agent once its implementation is complete
# from src.agents.researcher.agent import root_agent as researcher_agent

# TODO: Refine this placeholder persona into a "Triage Specialist". 
# It should be instructed to accurately determine user intent (e.g., medical query, appointment, research)
# and delegate to the appropriate sub-agent while maintaining context.
system_prompt = "You are a master agent. Talk to doctor or receptionist if needed."

app_name = os.getenv("APP_NAME", "hospital").lower().replace("-", "_")

# This agent connects the others as tools (Agent-as-a-Tool)
root_agent = Agent(
    name=f"{app_name}_master_agent",
    model="gemini-2.0-flash-lite",
    instruction=system_prompt,
    # TODO: Register the researcher_agent as an AgentTool once it is ready
    tools=[
        AgentTool(agent=doctor_agent),
        AgentTool(agent=receptionist_agent),
        # AgentTool(agent=researcher_agent),
    ],
    generate_content_config=types.GenerateContentConfig(temperature=0), 
)
