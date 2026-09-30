def is_even(number):
    """Return True when number is even."""
    return number % 2 == 0


def calculate_discount(price, discount_percent):
    """Return the price after applying a percentage discount."""
    if price < 0:
        raise ValueError("price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount must be between 0 and 100")
    return price - (price * discount_percent)


def find_longest_word(words):
    """Return the longest word in a non-empty list."""
    return max(words)


def safe_divide(dividend, divisor):
    """Divide two numbers and let division-by-zero errors be visible."""
    return dividend / divisor
