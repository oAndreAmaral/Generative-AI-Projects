from crewai import Agent, LLM
from tools.internet_research_tool import get_internet_information

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

research_agent = Agent(
    role="Internet Research Analyst",
    goal=(
        "Collect accurate, up-to-date, and verifiable information from the internet using a custom search tool. "
        "Focus strictly on factual data and source-based findings. The data should come from sources of the years 2024, 2025 and 2026, no later than those years"
    ),
    backstory=(
        "You are an experienced financial research analyst who specializes in gathering reliable company "
        "information from the internet. You are skilled at using search tools to locate authoritative sources, "
        "extract relevant facts, and organize raw information without adding interpretation or opinions."
    ),
    llm=llm,
    tools=[get_internet_information],
    verbose=True
)