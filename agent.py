from google.adk.agents import SequentialAgent, ParallelAgent

from google.adk.agents import agent_tool


# Root agent acting as a Workload coordinator
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name="Workforce",
    instruction=f"""
    Acts as a comprehensive trip planner.
    - Use the FlightAgent to find and book flights
    - Use the HotelAgent to find and book accommodation
    - Use the SightSeeingAgent to find information on places to visit
    ...
    """,
    sub_agents=[flight_agent, hotel_agent, sightseeing_agent] # The coordinator manages these sub-agents
)


from Client_onboarding.client import ClientonboardingAgent
from Project_management.project import ProjectAgent
from Sales_management.sales import SalesAgent

# Convert specialized agents into AgentTools
Clientonboarding_tool = agent_tool.AgentTool(agent=ClientonboardingAgent)
Project_tool = agent_tool.AgentTool(agent=ProjectAgent)
Sales_tool = agent_tool.AgentTool(agent=SalesAgent)


# Root agent now uses these agents as tools
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name="Workforce",
    instruction=f"""Enhances decision-making in Consulting Firm...
    By automating routine tasks, improving data management through sequentially invoke the tools to gather all necessary details...""",
    
    tools=[flight_tool, hotel_tool, sightseeing_tool] # The root agent can use these tools
)

