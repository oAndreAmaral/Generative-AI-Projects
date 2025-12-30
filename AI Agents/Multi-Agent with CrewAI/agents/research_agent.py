from crewai import Agent, LLM
from tools.internet_research_tool import get_internet_information

# Initialize the LLM
llm = LLM(
    model ="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

research_agent = Agent(
    role="Internet Research Analyst",
    goal=(
        "Conduct thorough internet-based research on a given {topic} by using the provided "
        "custom search tool 'get_internet_information. Gather, filter, and summarize reliable information from multiple "
        "sources to produce clear, well-structured findings."
    ),
    backstory=(
        "You are an experienced research analyst specializing in online information gathering. "
        "You are skilled at using custom search tools to locate relevant web sources, extract key "
        "details, compare perspectives, and synthesize accurate, concise insights from raw internet data."
    ),
    llm=llm,
    tools=[get_internet_information],
    verbose=True
)