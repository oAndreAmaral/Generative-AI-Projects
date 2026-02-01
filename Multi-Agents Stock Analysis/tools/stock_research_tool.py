import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol:str) -> str:

    """
    Gets the latest stock price for a given stock symbol using yahoo Finance.

    Input: stock_symbol:str | The ticker of the stock
    Output: str | Value of the current stock price, daily change and currency
    """

    stock = yf.Ticker(stock_symbol)

    current_price = stock.info.get("regularMarketPrice")
    change = stock.info.get("regularMarketChange")
    change_percent = stock.info.get("regularMarketChangePercent")
    currency = stock.info.get("currency", "USD")

    if current_price is None:
        return f"Could not find the price. Provide a correct symbol"
    
    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Change: {change} ({round(change_percent, 2)}%)\n"
    )
