"""Dynamic programming

This module implements dynamic programming
with two approaches, memoization, and
tabulation.

Functions:
    fibonacci_recursive: Calculates a Fibonacci number using recursion.
    fibonacci_memoization: Calculates a Fibonacci number using memoization.
    fibonacci_tabulation: Calculates a Fibonacci number using tabulation.
"""
def fibonacci_recursive(number: int) -> int:
    """Calculates the Fibonacci number for a given number using recursion.

    Attributes:
        number (int): Number to Fibonacci number for.

    Returns:
        int: Fibonacci number.
    """
    # Base case
    if number in (1, 2):
        return 1

    # Recursive case
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)

def fibonacci_memoization(number: int, store: list) -> int:
    """Calculates the fibonacci number for a given number
    using dynamic programming and the memoization
    approach (top to bottom).

    Accessing the store is number - 1 due to a list
    starting at 0, not 1.

    Attributes:
        number (int): Number to Fibonacci number for.
        store (list): List with pre-computed values.

    Returns:
        int: Fibonacci number.
    """
    # Check store to see if value is available
    if store[number - 1]:
        return store[number - 1]

    # Base case
    if number in (1, 2):
        result = 1
    # Recursive case
    else:
        result = fibonacci_memoization(number - 1, store) + fibonacci_memoization(number - 2, store)

    # Store the result for later use
    store[number - 1] = result

    return result

def fibonacci_tabulation(number: int) -> int:
    """Calculates the fibonacci number for a given number
    using dynamic programming and the tabulation
    approach (bottom to top).

    Accessing the store is number - 1 due to a list
    starting at 0, not 1.

    Attributes:
        number (int): Number to Fibonacci number for.

    Returns:
        int: Fibonacci number.
    """
    if number in (1, 2):
        return 1

    # Create the store to hold computed values
    store = [None] * number
    store[0] = 1
    store[1] = 1

    # Calculate the values up to number
    for index in range(2, number):
        store[index] = store[index - 1] + store[index - 2]

    return store[number - 1]
