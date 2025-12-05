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

from Client_onboarding/client.py import 
# Convert specialized agents into AgentTools
flight_tool = agent_tool.AgentTool(agent=flight_agent)
hotel_tool = agent_tool.AgentTool(agent=hotel_agent)
sightseeing_tool = agent_tool.AgentTool(agent=sightseeing_agent)



# Root agent now uses these agents as tools
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name="TripPlanner",
    instruction=f"""Acts as a comprehensive trip planner...
    Based on the user request, sequentially invoke the tools to gather all necessary trip details...""",
    
    tools=[flight_tool, hotel_tool, sightseeing_tool] # The root agent can use these tools
)



# 1. Create a parallel agent for concurrent tasks
plan_parallel = ParallelAgent(
    name="ParallelTripPlanner",
    sub_agents=[flight_agent, hotel_agent], # These run in parallel
)

# 2. Create a summary agent to gather results
trip_summary = LlmAgent(
    name="TripSummaryAgent",
    instruction="Summarize the trip details from the flight, hotel, and sightseeing agents...",
    output_key="trip_summary")

# 3. Create a sequential agent to orchestrate the full workflow
root_agent = SequentialAgent(
    name="PlanTripWorkflow",
    # Run tasks in a specific order, including the parallel step
    sub_agents=[sightseeing_agent, plan_parallel, trip_summary])
