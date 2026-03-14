VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    s = symbol.strip().upper()
    if not s:
        raise ValueError("Symbol cannot be empty.")
    return s


def validate_side(side):
    s = side.strip().upper()
    if s not in VALID_SIDES:
        raise ValueError(f"Invalid side '{side}'. Must be BUY or SELL.")
    return s


def validate_order_type(order_type):
    ot = order_type.strip().upper()
    if ot not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type '{order_type}'. Must be one of: {', '.join(VALID_ORDER_TYPES)}")
    return ot


def validate_quantity(qty):
    try:
        q = float(qty)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid quantity: {qty}")
    if q <= 0:
        raise ValueError("Quantity must be positive.")
    return q


def validate_price(price):
    if price is None:
        return None
    try:
        p = float(price)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid price: {price}")
    if p <= 0:
        raise ValueError("Price must be positive.")
    return p
