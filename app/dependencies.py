from binance.client import Client

API_KEY = "your_binance_api_key"
API_SECRET = "your_binance_secret_key"

def get_binance_client():
    return Client(API_KEY, API_SECRET)
