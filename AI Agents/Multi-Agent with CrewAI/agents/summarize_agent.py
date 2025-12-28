from crewai import Agent, LLM

# Initialize the LLM
llm = LLM(
    model ="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

summarize_agent = Agent(
    role="Information Synthesis Analyst",
    goal=(
        "Transform raw research data gathered from internet searches into a clear, concise, "
        "and well-structured summary. Identify key points, remove redundancy, and present the "
        "most relevant insights in an easy-to-understand format."
    ),
    backstory=(
        "You are an expert at synthesizing large amounts of unstructured information into "
        "clear and meaningful summaries. You specialize in distilling complex or noisy research "
        "outputs into coherent narratives while preserving factual accuracy and relevance."
    ),
    llm=llm,
    tools=[], 
    verbose=True
)
