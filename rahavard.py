import requests
from config import HEADERS

BASE_URL = "https://rahavard365.com/api/v2"


def get_asset(asset_id):
    url = f"{BASE_URL}/asset/{asset_id}"
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()


def get_price(asset_id):
    data = get_asset(asset_id)

    return {
        "name": data.get("symbol", ""),
        "last": data.get("lastPrice"),
        "close": data.get("closingPrice"),
        "change": data.get("priceChange"),
        "percent": data.get("priceChangePercent"),
    }
