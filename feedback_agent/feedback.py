# Agent to check if the trip summary meets quality standards
trip_summary_reviewer = LlmAgent(
    name="TripSummaryReviewer",
    instruction=f"""Review the trip summary in {{trip_summary}}.
    If the summary meets quality standards, output 'pass'. If not, output 'fail'""",
    output_key="review_status", # Writes its verdict to a new key
)

# Custom agent to check the status and provide feedback

class ValidateTripSummary(BaseAgent):
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        status = ctx.session.state.get("review_status", "fail")
        review = ctx.session.state.get("trip_summary", None)
        if status == "pass":
            yield Event(author=self.name, content=Content(parts=[Part(text=f"Trip summary review passed: {review}")]))
        else:
            yield Event(
                content=Content(parts=[Part(author=self.name,
  text="Trip summary review failed. Please provide a valid requirements")]))
ValidateTripSummaryAgent = ValidateTripSummary(
    name="ValidateTripSummary",
    description="Validates the trip summary review status and provides feedback based on the review outcome.",)

# The final, self-regulating workflow
root_agent = SequentialAgent(
    name="PlanTripWorkflow",
    sub_agents=[
        sightseeing_agent,
        plan_parallel,
        trip_summary,
        trip_summary_reviewer,
        ValidateTripSummaryAgent() # The final validation step 
])
