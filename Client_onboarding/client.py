from google.adk.agents import LlmAgent

# Flight Agent: Specializes in flight booking and information
flight_agent = LlmAgent(
    model='gemini-2.0-flash',
    name="FlightAgent",
    description="Flight booking agent",
    instruction=f"""You are a flight booking agent... You always return a valid JSON...""")
