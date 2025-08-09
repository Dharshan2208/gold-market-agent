from langgraph_flow import compiled_graph


# Run agent directly
def run_market_analysis():
    print("[Gold Market Agent] Running full analysis...\n")

    result = compiled_graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    # "content": "Analyze why the gold rate increased or decreased recently using latest price give dates also and news data and also mention the exact price data.",
                    "content": (
                        "You are a financial analyst. Based on the following information:\n\n"
                        "1. Current gold price (in USD)\n"
                        "2. Historical gold prices for the last 10 days (with dates and prices)\n"
                        "3. Recent news headlines and summaries related to gold price movements\n\n"
                        "Please analyze and explain:\n"
                        "- Whether the gold price has increased, decreased, or remained stable over this 10-day period\n"
                        "- The major events or reasons driving this change (e.g., inflation news, interest rate decisions, geopolitical tensions)\n"
                        "- Quote the specific dates and price points where significant movement occurred\n"
                        "- Provide a clear summary in 4-5 bullet points\n\n"
                        "Ensure your response is structured, factual, and uses both the price data and news context."
                    ),
                }
            ]
        }
    )

    final_message = result["messages"][-1]
    print("\n[Gold Market Analysis Result]:\n")
    print(final_message.content)


if __name__ == "__main__":
    run_market_analysis()
