from crewai import Task
from agents.trader_agent import trader_agent
from tasks.summary_task import summary_task
from tasks.analyse_task import stock_analysis

trade_decision = Task(
    description=(
        "Using the provided company summary and stock market data for {stock}, "
        "decide whether the appropriate action is Buy, Hold, or Sell.\n\n"
        "Base your decision ONLY on the supplied inputs. Do NOT fetch new data."
    ),
    context=[summary_task, stock_analysis],
    expected_output=(
        "A structured trading decision with the following fields:\n\n"
        "- recommendation: Buy | Hold | Sell\n"
        "- confidence_level: Low | Medium | High\n"
        "- reasoning:\n"
        "  - company_fundamentals_summary\n"
        "  - market_data_observations\n"
        "  - risk_factors\n"
        "- time_horizon: Short-term | Medium-term\n\n"
        "The recommendation must be logically consistent with the provided data."
    ),
    agent=trader_agent
)