#!/usr/bin/env python3
"""Simple macOS menu bar app to display stock or futures prices using the Moomoo OpenAPI."""

import os
import requests
import rumps

API_ENDPOINT = os.getenv("MOOMOO_API_ENDPOINT", "https://openapi.moomoo.com/v1/market/quote")
API_TOKEN = os.getenv("MOOMOO_API_TOKEN", "")
SYMBOL = os.getenv("MOOMOO_SYMBOL", "AAPL")
REFRESH_INTERVAL = int(os.getenv("REFRESH_INTERVAL", "60"))  # seconds


def fetch_price(symbol: str) -> str:
    """Fetch the latest price for the given symbol from the Moomoo OpenAPI."""
    headers = {"Authorization": f"Bearer {API_TOKEN}"} if API_TOKEN else {}
    params = {"symbol": symbol}
    try:
        response = requests.get(API_ENDPOINT, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        # Adjust the key paths below based on the actual API response structure.
        return str(data["data"][0]["last_price"])
    except Exception:
        return "N/A"


class StockTickerApp(rumps.App):
    """Menu bar app that periodically updates the displayed price."""

    def __init__(self, symbol: str) -> None:
        super().__init__(symbol)
        self.symbol = symbol
        self.menu = ["Refresh"]
        self.timer = rumps.Timer(self.refresh, REFRESH_INTERVAL)
        self.timer.start()
        self.refresh(None)

    def refresh(self, _):
        price = fetch_price(self.symbol)
        self.title = f"{self.symbol} {price}"

    @rumps.clicked("Refresh")
    def manual_refresh(self, _):
        self.refresh(None)


def main() -> None:
    StockTickerApp(SYMBOL).run()


if __name__ == "__main__":
    main()
