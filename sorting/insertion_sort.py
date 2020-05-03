"""Insertion sort

This module implements the insertion sort algorithm.

Functions:
    insertion_sort: Implementation of insertion sort.
"""
from typing import List

def insertion_sort(elements: List) -> List:
    """Sorts a list using the insertion sort algorithm.

    Pass through the list of elements placing smaller
    elements to their correct position in the sorted
    left side of the list.

    Args:
        elements (list): Unordered list of elements.

    Returns:
        list: Ordered list of elements.
    """
    # Pass through the list of elements and assume the first
    # element is already sorted (range start = 1).
    for element in range(1, len(elements)):
        element_value = elements[element]
        pointer = element - 1

        # Compare element to ordered sublist, checking if the
        # value of element is less than or equal to the
        # ordered elements.
        while pointer >= 0 and elements[pointer] > element_value:
            # Move larger valued ordered element one position
            # to the right.
            elements[pointer + 1] = elements[pointer]
            # Move along the ordered sublist from right to left
            pointer -= 1

        # Insert element to the right of the lower valued
        # ordered element.
        elements[pointer + 1] = element_value

    return elements
