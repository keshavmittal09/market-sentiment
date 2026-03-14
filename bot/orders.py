from binance.enums import *
from bot.logging_config import get_logger

logger = get_logger(__name__)


def place_market_order(client, symbol, side, quantity):
    logger.info(f"Placing MARKET {side} order for {symbol}, qty={quantity}")
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity,
        )
        logger.info(f"Order response: {order}")
        return order
    except Exception as e:
        logger.error(f"MARKET order failed: {e}")
        raise


def place_limit_order(client, symbol, side, quantity, price):
    logger.info(f"Placing LIMIT {side} order for {symbol}, qty={quantity}, price={price}")
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC,
        )
        logger.info(f"Order response: {order}")
        return order
    except Exception as e:
        logger.error(f"LIMIT order failed: {e}")
        raise


def place_stop_limit_order(client, symbol, side, quantity, price, stop_price):
    logger.info(f"Placing STOP_LIMIT {side} order for {symbol}, qty={quantity}, price={price}, stop={stop_price}")
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce=TIME_IN_FORCE_GTC,
        )
        logger.info(f"Order response: {order}")
        return order
    except Exception as e:
        logger.error(f"STOP_LIMIT order failed: {e}")
        raise
