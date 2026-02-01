from crewai import Agent, LLM

# Initialize the LLM
llm = LLM(
    model ="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

summarize_agent = Agent(
    role="Information Synthesis Analyst",
    goal=(
        "Convert raw research data into a clear, neutral, and well-structured summary "
        "without adding new information or opinions."
    ),
    backstory=(
        "You specialize in synthesizing raw research into readable, decision-ready summaries. "
        "You preserve factual accuracy, remove redundancy, and improve clarity while strictly "
        "respecting the source material."
    ),
    llm=llm,
    tools=[],
    verbose=False
)
