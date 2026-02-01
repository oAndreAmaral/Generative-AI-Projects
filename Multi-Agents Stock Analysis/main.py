import os
import time
from dotenv import load_dotenv
from crew import stock_crew

load_dotenv()

def run_simple(topic: str, stock: str):
    """
    Kick off the stock Crew pipeline with a topic and stock ticker.

    Args:
        topic (str): The company/topic to research.
        stock (str): The stock ticker to analyze.
    """
    # Run the CrewAI pipeline with both inputs
    result = stock_crew.kickoff(inputs={
        "topic": topic,
        "stock": stock
    })

    # Print the structured output
    print("=== CrewAI Output ===")
    print(result)

if __name__ == "__main__":

    stock = "IOVA"
    topic = "Latest financial and market analysis for IOVA"

    run_simple(topic, stock)
    
 