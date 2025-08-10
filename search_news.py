from langchain_tavily import TavilySearch
# from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

search_tool = TavilySearch(max_results=10, return_direct=True)


# Create the base Tavily object
# base_search = TavilySearch(max_results=10)


# @tool
# def search_gold_news() -> str:
#     """
#     Searches for recent news specifically related to gold price movements and market trends.
#     This includes geopolitical influences, inflation, interest rates, etc.
#     """
#     query = "recent news about gold price increase or decrease"

#     search_tool = TavilySearch(
#         max_results=10,
#         return_direct=True,
#         search_window="2d",
#     )

#     return search_tool.invoke({"query": query})