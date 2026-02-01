from crewai import Task
from agents.summarize_agent import summarize_agent
from tasks.research_task import research_task

summary_task = Task(
    description=(
        "Using ONLY the research data provided, create a clear, concise, and well-structured summary "
        "of the topic: {topic}.\n\n"
        "Do NOT introduce new facts, opinions, or assumptions. Do NOT perform financial analysis.\n"
        "Focus on clarity, relevance, and factual accuracy."
    ),
    context=[research_task],
    expected_output=(
        "A structured summary with the following sections:\n\n"
        "- company_overview: plain-language description of the company\n"
        "- key_financial_points: simplified explanation of financial performance\n"
        "- recent_events: notable news or developments\n"
        "- strengths_and_risks: factual strengths and risks mentioned in the research\n\n"
        "All content must be derived strictly from the research input."
    ),
    agent=summarize_agent
)