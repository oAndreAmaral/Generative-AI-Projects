from crewai import Agent, LLM
from tools.stock_research_tool import get_stock_price

# Initialize the LLM
llm = LLM(
    model ="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

analyst_agent = Agent(
    role="Financial Market Data Analyst",
    goal=(
        "Retrieve and describe real-time stock market data using live price tools. "
        "Focus strictly on factual market metrics and observable price behavior."
    ),
    backstory=(
        "You are an experienced market data analyst specializing in interpreting real-time stock prices, "
        "volume, and volatility. You report objective observations without making investment recommendations."
    ),
    llm=llm,
    tools=[get_stock_price],
    verbose=False
)