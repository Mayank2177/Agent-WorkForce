from google.adk.agents import LlmAgent

# Sightseeing Agent: Specializes in providing sightseeing recommendations
sightseeing_agent = LlmAgent(
    model='gemini-2.0-flash',
    name="SightseeingAgent",
    description="Sightseeing information agent",
    instruction=f"""You are a sightseeing information agent... You always return a valid JSON...""")
