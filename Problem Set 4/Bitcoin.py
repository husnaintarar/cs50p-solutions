import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    number = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=baba504df8c1d051a31a285352040eae48c8ce23726d007e8d3c67cfbe1d4bec")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    total_cost = price * number
    print(f"${total_cost:,.4f}")

except requests.RequestException:
    sys.exit("Error: Could not connect to the API")