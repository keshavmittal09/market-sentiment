import argparse
import sys
from bot.client import get_client
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.orders import place_market_order, place_limit_order, place_stop_limit_order
from bot.logging_config import get_logger

logger = get_logger("cli")


def build_parser():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, dest="order_type", help="MARKET, LIMIT, or STOP_LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, default=None, help="Required for LIMIT and STOP_LIMIT orders")
    parser.add_argument("--stop-price", type=float, default=None, help="Required for STOP_LIMIT orders")
    return parser


def show_summary(symbol, side, order_type, quantity, price=None, stop_price=None):
    print("\n--- Order Request ---")
    print(f"  Symbol:   {symbol}")
    print(f"  Side:     {side}")
    print(f"  Type:     {order_type}")
    print(f"  Quantity: {quantity}")
    if price:
        print(f"  Price:    {price}")
    if stop_price:
        print(f"  Stop:     {stop_price}")
    print("---------------------")


def show_response(resp):
    print("\n--- Order Response ---")
    print(f"  Order ID:     {resp.get('orderId')}")
    print(f"  Status:       {resp.get('status')}")
    print(f"  Executed Qty: {resp.get('executedQty')}")
    avg = resp.get("avgPrice", "N/A")
    print(f"  Avg Price:    {avg}")
    print("----------------------")


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)
    except ValueError as e:
        print(f"Validation error: {e}")
        sys.exit(1)

    if order_type == "LIMIT" and price is None:
        print("Error: --price is required for LIMIT orders.")
        sys.exit(1)

    stop_price = None
    if order_type == "STOP_LIMIT":
        if price is None or args.stop_price is None:
            print("Error: --price and --stop-price are both required for STOP_LIMIT orders.")
            sys.exit(1)
        try:
            stop_price = validate_price(args.stop_price)
        except ValueError as e:
            print(f"Validation error: {e}")
            sys.exit(1)

    show_summary(symbol, side, order_type, quantity, price, stop_price)

    try:
        client = get_client()

        if order_type == "MARKET":
            resp = place_market_order(client, symbol, side, quantity)
        elif order_type == "LIMIT":
            resp = place_limit_order(client, symbol, side, quantity, price)
        elif order_type == "STOP_LIMIT":
            resp = place_stop_limit_order(client, symbol, side, quantity, price, stop_price)
        else:
            print(f"Unsupported order type: {order_type}")
            sys.exit(1)

        show_response(resp)
        logger.info("Order placed successfully")
        print("\nOrder placed successfully!")

    except Exception as e:
        logger.error(f"Order failed: {e}")
        print(f"\nOrder failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
