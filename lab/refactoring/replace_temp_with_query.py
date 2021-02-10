# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
"""
Gets price of an order based on item_price and quantity
"""

def get_price(quantity, item_price):
    """Gets total price for an order"""
    base_price = quantity * item_price
    discount_factor = get_dis_factor(item_price)

    return base_price * discount_factor

def get_dis_factor(base_price):
    """Gets discount factor based on price"""
    if base_price > 1000:
        return 0.95
    return 0.98

print(get_price(5, 10))
