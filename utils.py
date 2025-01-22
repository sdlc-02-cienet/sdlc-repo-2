"""
utils.py
A collection of helper functions.
"""

def add_numbers(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.
    """
    return a + b

def greet(name: str) -> str:
    """
    Returns a greeting message. If name is empty or None,
    defaults to 'Hello, there!'.
    """
    if not name:
        return "Hello, there!"
    return f"Hello, {name}!"