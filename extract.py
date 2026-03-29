import pandas as pd
import requests
import os
from datetime import datetime

# Current market data per the API documentation
url = "https://api.coingecko.com/api/v3/coins/markets"

# URL parameters passed in the request
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}

# Coin Gecko operates utilizing the API key as a header.
headers = {'x-cg-demo-api-key': os.getenv("COINGECKO_API_KEY")}

""" 
Primary extraction function that utilizes a GET request to pull the data,
assign it as a JSON, turn the JSON into a Pandas DataFrame, assign a datetime,
and finally return the dataframe.
"""
def extract_data():
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data)

        df = df[[
                "id",
                "symbol",
                "name",
                "current_price",
                "market_cap",
                "total_volume",
                "price_change_percentage_24h"
                 ]]
        df["ingested_at"] = datetime.now()

        return df

    except Exception as e:
        print(f"Error: {e}")
        return None
