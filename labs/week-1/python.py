import requests
import json

# Endpoint and headers
url = "https://api.coingecko.com/api/v3/coins/markets"
headers = {"x-cg-demo-api-key": "CG-He1BkdgSLTNHx4cMkBgriKHx "}  # Replace with your actual key

# Parameters
params = {
    "vs_currency": "usd",
    "per_page": 5,
    "page": 1
}

# Make the request
response = requests.get(url, headers=headers, params=params)

# Parse response
if response.status_code == 200:
    data = response.json()

    # Print the full JSON (pretty formatted)
    print(json.dumps(data, indent=2))

    # Loop through coins and print specific fields
    print("\n--- Coin Info ---")
    for coin in data:
        print(f"ID: {coin['id']}, Symbol: {coin['symbol']}, Price: ${coin['current_price']}")
else:
    print(f"Error: {response.status_code}, {response.text}")