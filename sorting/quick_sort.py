"""Quick sort

This module implements the quick sort algorithm.

Functions:
    quick_sort: Implementation of quick sort.
"""
from random import randint
from typing import List

def quick_sort(elements: List) -> List:
    """Sorts a list using the quick sort algorithm.

    Recursively break the list of elements based on
    a random pivot value and then merge back 
    together in order.

    Args:
        elements (list): Unordered list of elements.

    Returns:
        list: Ordered list of elements.
    """
    # Base case - completed splitting the list
    if len(elements) <= 1:
        return elements

    # Recursive case
    low_list = []
    same_list = [] # For elements that equal the pivot value
    high_list = []

    # Select the pivot value from elements using a random integer
    pivot_value = elements[randint(0, len(elements) - 1)]

    # Sort elements based on the pivot_value value
    for element in elements:
        if element < pivot_value:
            low_list.append(element)
        elif element == pivot_value:
            same_list.append(element)
        elif element > pivot_value:
            high_list.append(element)

    ordered_low_list = quick_sort(low_list)
    ordered_high_list = quick_sort(high_list)

    return ordered_low_list + same_list + ordered_high_list
