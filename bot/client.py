import os
import time
import requests
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

TESTNET_BASE = "https://testnet.binancefuture.com"


def _get_server_time():
    resp = requests.get(f"{TESTNET_BASE}/fapi/v1/time")
    return resp.json()["serverTime"]


def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API credentials missing. Check your .env file.")

    client = Client(api_key, api_secret, testnet=True)

    server_time = _get_server_time()
    local_time = int(time.time() * 1000)
    client.timestamp_offset = server_time - local_time

    return client
