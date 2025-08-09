from typing import Annotated
from typing_extensions import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from gold_price import get_gold_price_info
from search_news import search_tool
# from search_news import search_gold_news
from analyser import analyze_market_data


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph = StateGraph(State)

graph.add_node("fetch_prices", get_gold_price_info)
graph.add_node("fetch_news", ToolNode(tools=[search_tool]))
# graph.add_node("fetch_news", ToolNode(tools=[search_gold_news]))
graph.add_node("analyze", analyze_market_data)


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.45)
price_analyst_tool = llm.bind_tools([search_tool])
# price_analyst_tool = llm.bind_tools([search_gold_news])


def price_analyst(state):
    return {"messages": [price_analyst_tool.invoke(state["messages"])]}


graph.add_node("price_analyst", price_analyst)

# Edges
graph.add_edge(START, "fetch_prices")
graph.add_edge("fetch_prices", "price_analyst")
graph.add_edge("price_analyst", "fetch_news")
graph.add_edge("fetch_news", "analyze")
graph.add_edge("analyze", END)

compiled_graph = graph.compile()
