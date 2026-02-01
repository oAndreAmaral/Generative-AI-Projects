from crewai import Task
from agents.analist_agent import analyst_agent

stock_analysis = Task(
    description=(
        "Use the stock data tool to retrieve real-time market data for the stock: {stock}.\n\n"
        "Report factual market metrics only. Do NOT provide investment advice or recommendations."
    ),
    expected_output=(
        "A structured market data report with the following fields:\n\n"
        "- current_price\n"
        "- daily_change (absolute and percentage)\n"
        "- trading_volume\n"
        "- volatility_observations (price movement only)\n"
        "- short_term_trend (descriptive, e.g., rising, falling, flat)\n\n"
        "All observations must be directly supported by the retrieved market data."
    ),
    agent=analyst_agent
)
