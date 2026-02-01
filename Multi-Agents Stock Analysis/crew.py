# How to combine the agents
from crewai import Crew

# Agents importation
from agents.research_agent import research_agent
from agents.summarize_agent import summarize_agent
from agents.analist_agent import analyst_agent
from agents.trader_agent import trader_agent

# Tasks importation
from tasks.research_task import research_task
from tasks.summary_task import summary_task
from tasks.analyse_task import stock_analysis
from tasks.trade_task import trade_decision

stock_crew = Crew(
    agents= [research_agent, summarize_agent, analyst_agent, trader_agent],
    tasks=[research_task, summary_task, stock_analysis, trade_decision],
    verbose=False
)