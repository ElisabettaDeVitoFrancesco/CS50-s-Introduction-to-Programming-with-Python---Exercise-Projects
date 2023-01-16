import sys
import requests
import json

# Check the command line input first
# If it's missing
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2: # If there are too many arguments (my idea)
    sys.exit("Too many arguments")
# If it is not a number
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Get the USD rate from the API with the requests package
api_bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
api_bitcoin_dict = api_bitcoin.json()
api_bitcoin_bpi_USD_rate = api_bitcoin_dict["bpi"]["USD"]["rate_float"]

# Calculate the USD value of n bitcoins, and print the value with , as thousand separator and . as decimal separator
bitcoin_USD_value = n * api_bitcoin_bpi_USD_rate
print(f"${bitcoin_USD_value:,.4f}")
