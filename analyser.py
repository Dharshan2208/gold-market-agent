from langchain_google_genai import ChatGoogleGenerativeAI


def analyze_market_data(state):
    """
    Analyzes gold price trends using LLM with historical data + news.
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.45)

    # Extract all the messages (including price and news results)
    messages = state["messages"]

    # Add a system-level summary instruction
    prompt = (
        "You are a financial analyst. Using the following data:\n"
        "- Gold prices for the past 10 days\n"
        "- Current gold price\n"
        "- News articles related to gold\n"
        "Please analyze and explain the key reasons why the gold price has increased or decreased."
        "\n\nRespond in a structured and clear format."
    )

    messages.insert(0, {"role": "system", "content": prompt})

    return {"messages": [model.invoke(messages)]}
