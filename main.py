"""
main.py
The main entry point for the fake repo example.
"""

import utils

def main():
    # Demonstrate the 'add_numbers' function
    result = utils.add_numbers(5, 7)
    print(f"The sum of 5 and 7 is: {result}")

    # Demonstrate the 'greet' function
    greeting_message = utils.greet("Alice")
    print(greeting_message)

if __name__ == "__main__":
    main()
