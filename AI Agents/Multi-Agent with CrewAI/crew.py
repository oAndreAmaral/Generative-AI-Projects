# How to combine the agents
from crewai import Crew
from agents.research_agent import research_agent
from agents.summarize_agent import summarize_agent
from tasks.research_task import research_task
from tasks.summary_task import summary_task

stock_crew = Crew(
    agents= [research_agent, summarize_agent],
    tasks=[research_task, summary_task],
    verbose=True
)