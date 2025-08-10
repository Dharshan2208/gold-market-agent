import os
import requests
from langchain_core.tools import tool
from langchain_core.messages import AIMessage


@tool
def get_gold_price_info() -> dict:
    """
    Fetches current gold price and historical gold price data for the past 10 days.
    """
    metal_price_key = os.environ.get("METAL_PRICE_API")
    alpha_key = os.environ.get("ALPHA_VANTAGE_API_KEY")

    try:
        # Current gold price from MetalPrice API
        metal_resp = requests.get(
            f"https://api.metalpriceapi.com/v1/latest?api_key={metal_price_key}&base=XAU&currencies=USD"
        )
        metal_resp.raise_for_status()
        metal_price = metal_resp.json()["rates"]["XAU"]

        # Historical gold prices (past 10 days) from Alpha Vantage
        alpha_resp = requests.get(
            f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOLD&apikey={alpha_key}"
        )
        alpha_resp.raise_for_status()
        time_series = alpha_resp.json().get("Time Series (Daily)", {})
        historical = dict(list(time_series.items())[:10])

        return AIMessage(
            content=(
                f"Current gold price: {metal_price}\n"
                f"Historical prices (last 10 days):\n{historical}"
            )
        )

    except Exception as e:
        return AIMessage(content=f"[ERROR] Failed to fetch gold prices: {str(e)}")
