from crewai import Task
from agents.summarize_agent import summarize_agent

summary_task = Task(
    description=(
        "Take the raw research data collected on the topic: {topic} and generate a clear, concise, "
        "and well-structured summary. Extract the most important insights, trends, and key points "
        "from the gathered information, removing redundancy or irrelevant details."
    ),
    expected_output=(
        "A structured, bullet-pointed summary including:\n"
        "- Main findings and key insights\n"
        "- Trends, patterns, or notable observations\n"
        "- Supporting evidence from the sources\n"
        "- Clear and readable format suitable for decision-making or reporting"
    ),
    agent=summarize_agent
)