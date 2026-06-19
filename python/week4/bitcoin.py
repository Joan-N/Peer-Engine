import requests
import sys

try:
    n = float(sys.argv[1])
except (IndexError, ValueError):
     sys.exit("Missing command-line argument")
    
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    print(f"${n * price:,.4f}")
except requests.RequestException:
    sys.exit("Network error")