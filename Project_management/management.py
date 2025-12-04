from google.adk.agents import LlmAgent

# Hotel Agent: Specializes in hotel booking and information
hotel_agent = LlmAgent(
    model='gemini-2.0-flash',
    name="HotelAgent",
    description="Hotel booking agent",
    instruction=f"""You are a hotel booking agent... You always return a valid JSON...""")
