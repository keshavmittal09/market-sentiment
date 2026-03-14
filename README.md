# Binance Futures Testnet Trading Bot

A command-line trading bot for placing orders on Binance Futures Testnet (USDT-M). Supports Market, Limit, and Stop-Limit orders with input validation and logging.

## Setup

1. Clone the repo:
```bash
git clone https://github.com/keshavmittal09/market-sentiment.git
cd market-sentiment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Binance Futures Testnet API credentials:
```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

You can get these from [https://testnet.binancefuture.com](https://testnet.binancefuture.com).

## Usage

### Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

### Stop-Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.01 --price 65000 --stop-price 66000
```

## Arguments

| Argument | Required | Description |
|---|---|---|
| `--symbol` | Yes | Trading pair (e.g., BTCUSDT) |
| `--side` | Yes | BUY or SELL |
| `--type` | Yes | MARKET, LIMIT, or STOP_LIMIT |
| `--quantity` | Yes | Order quantity |
| `--price` | For LIMIT/STOP_LIMIT | Limit price |
| `--stop-price` | For STOP_LIMIT | Trigger price for stop-limit |

## Project Structure

```
market-sentiment/
  bot/
    __init__.py
    client.py           -> Binance client wrapper
    orders.py           -> order placement logic
    validators.py       -> input validation
    logging_config.py   -> logging setup
  cli.py                -> CLI entry point
  requirements.txt
  .env.example
```

## Logging

All API requests, responses, and errors are logged to `logs/trading_bot.log`. The log file is created automatically on the first run.

## Assumptions

- This bot is designed for Binance Futures Testnet only (USDT-M).
- API credentials are loaded from a `.env` file and are not committed to version control.
- The `python-binance` library handles request signing and testnet routing internally.
- Quantity values should follow Binance's lot size rules for the given symbol.
