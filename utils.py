"""
utils.py
A collection of helper functions.
"""

def add_numbers(a, b=None):
    """
    Returns the sum of either:
      - Two numbers: add_numbers(1.0, 2.0)
      - A list of numbers: add_numbers([1.0, 2.0, 3.0])
    """
    if isinstance(a, list):
        # If 'a' is actually a list, just sum its items
        return sum(a)

    # If 'a' isn't a list, assume we have two separate numbers
    if b is None:
        raise ValueError("Second argument must be provided if the first isn't a list.")

    return a + b

def greet(name: str) -> str:
    """
    Returns a greeting message. If name is empty or None,
    defaults to 'Hello, there!'.
    """
    if not name:
        return "Hello, there!"
    return f"Hello, {name}!"