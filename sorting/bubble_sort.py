"""Bubble sort

This module implements several versions
of the bubble sort algorithm to sort
an unordered list.

Functions:
    bubble_sort: Standard bubble sort implementation
    short_bubble_sort: Optimised bubble sort implementation
"""
from typing import List

def bubble_sort(elements: List) -> List:
    """Performs a bubble sort on a list of elements.

    Pass through the elements several times,
    comparing the elements and performing
    swaps so that larger elements move
    towards the end of the list.

    Args:
        elements (list): Unordered list of elements.

    Returns:
        list: Ordered list of elements.
    """
    number_elements = len(elements)

    # For each element in the list, make a
    # pass through the list of elements
    for number_passes in range(number_elements):
        # Iterate through the elements, except for the last element
        # as it is compared inside the loop. Reduce the iteration
        # of elements from right to left as the number of passes
        # increases, due to smaller valued elements falling to
        # the start of the list.
        for element in range(number_elements - (number_passes + 1)):
            # Swap the elements if the current element
            # is larger than the element to its right.
            if elements[element] > elements[element + 1]:
                elements[element], elements[element + 1] \
                    = elements[element + 1], elements[element]

    return elements

def short_bubble_sort(elements: List) -> List:
    """Performs a bubble sort on a list of elements
    using an optimised version of the algorithm.

    Pass through the list of elements several times,
    each time checking whether the list has become
    sorted.

    Args:
        elements (list): Unordered list of elements.

    Returns:
        list: Ordered list of elements.
    """
    number_elements = len(elements)

    for number_passes in range(number_elements):
        # Flag to detect if the list is sorted
        is_sorted = True

        for element in range(number_elements - (number_passes + 1)):

            if elements[element] > elements[element + 1]:
                elements[element], elements[element + 1] \
                    = elements[element + 1], elements[element]
                # As a change has been made, the
                # list may not be sorted.
                is_sorted = False

        # If the list is sorted, stop
        # making unnecessary passes.
        if is_sorted:
            break

    return elements
