# testing

## Hello World Program

A basic C program demonstrating how to print "Hello, world!".

### Build and Run

```sh
gcc hello.c -o hello
./hello
```

## macOS Menu Bar Stock/Futures Ticker

A simple Python script that displays the latest price for a configured symbol in the macOS menu bar. It uses the [Moomoo OpenAPI](https://www.moomoo.com) to fetch prices.

### Requirements

- macOS
- Python 3
- [`rumps`](https://pypi.org/project/rumps/) and [`requests`](https://pypi.org/project/requests/)

Install dependencies:

```sh
pip install rumps requests
```

### Usage

Set the necessary environment variables and run the script:

```sh
export MOOMOO_API_TOKEN="YOUR_API_TOKEN"
export MOOMOO_SYMBOL="AAPL"  # or any other stock/futures symbol
python stock_menu_bar.py
```

The ticker updates every 60 seconds by default. Adjust the `REFRESH_INTERVAL` environment variable to change the refresh rate.

