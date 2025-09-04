"""
Assignment 1 Web Search Tool
Uses Tavily API for real search results.
No OpenAI API key required.
"""

import os
from tavily import TavilyClient
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Initialize Tavily client
tavily = TavilyClient(api_key=TAVILY_API_KEY)

# Function to search the web
def search_web(query: str):
    results = tavily.search(query, max_results=3)
    return [r["url"] for r in results["results"]]

# Main loop
if __name__ == "__main__":
    print("Tavily Web Search running (type quit to exit)")
    while True:
        q = input("You: ")
        if q.lower() == "quit":
            break
        urls = search_web(q)
        print("Bot: I found these sources ->", urls)
