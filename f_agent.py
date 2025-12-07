"""
# 1. Create a parallel agent for concurrent tasks
plan_parallel = ParallelAgent(
    name="ParallelTripPlanner",
    sub_agents=[flight_agent, hotel_agent], # These run in parallel
)

# 2. Create a summary agent to gather results
trip_summary = LlmAgent(
    name="TripSummaryAgent",
    instruction="Summarize the Work details from the Client Onboarding, Project, Sales agents...",
    output_key="work_summary")

# 3. Create a sequential agent to orchestrate the full workflow
root_agent = SequentialAgent(
    name="PlanTripWorkflow",
    # Run tasks in a specific order, including the parallel step
    sub_agents=[sightseeing_agent, plan_parallel, trip_summary])
"""
