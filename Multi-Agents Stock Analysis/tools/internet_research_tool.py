import requests
import os
from crewai.tools import tool

@tool("Live Internet Searcher")
def get_internet_information(query, SERPAPI_KEY, num_results=5) -> str:

    """
    Searches the internet for information on a given query using SerpAPI
    and returns a list of search results with title, link, and snippet.
    
    Parameters:
    - query (str): The search query/topic.
    - SERPAPI_KEY (str): Your SerpAPI API key.
    - num_results (int): Number of search results to return.

    Returns:
    - List[Dict]: A list of dictionaries containing 'title', 'link', and 'snippet' for each result.
    """
    SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
    
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERPAPI_KEY,
        "num": num_results
    }

    response = requests.get(url, params=params)
    data = response.json()

    # 🔍 DEBUG: check for errors
    if "error" in data:
        print("API ERROR:", data["error"])
        return []

    if "organic_results" not in data:
        print("No organic_results found.")
        print("Full response:", data)
        return []

    results = []
    for result in data["organic_results"]:
        results.append({
            "title": result.get("title"),
            "link": result.get("link"),
            "snippet": result.get("snippet")
        })

    return results