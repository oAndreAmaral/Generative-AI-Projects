from crewai import Task
from agents.research_agent import research_agent

research_task = Task(
    description=(
        "Conduct thorough internet research on the topic: {topic}. Use the custom internet search tool 'get_internet_information'"
        "to retrieve relevant information, including articles, summaries, and key points from multiple sources. "
        "Gather enough data to provide a comprehensive overview of the topic."
    ),
    expected_output=(
        "A structured, bullet-pointed summary including:\n"
        "- Key facts and insights from multiple sources\n"
        "- Relevant statistics or examples\n"
        "- Main trends, patterns, or themes\n"
        "- Links or citations to the original sources"
    ),
    agent=research_agent
)