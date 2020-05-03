"""Merge sort

This module implements the merge sort algorithm.

Functions:
    merge_sort: Implementation of merge sort.
"""
from typing import List

def merge_sort(elements: List) -> List:
    """Sorts a list using the merge sort algorithm.

    Recursively break the list of elements in half
    and then merge them back together in order.

    Args:
        elements (list): Unordered list of elements.

    Returns:
        list: Ordered list of elements.
    """
    # Base case - completed splitting the list
    if len(elements) <= 1:
        return elements

    # Recursive case
    middle_element = len(elements) // 2

    # Split left side of the list
    left_list = merge_sort(elements[:middle_element])
    # Split right side of the list
    right_list = merge_sort(elements[middle_element:])

    left_index = 0
    right_index = 0
    ordered_list = []

    # Loop throught the elements of each list and order
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            # Add the smaller left element to ordered_list
            ordered_list.append(left_list[left_index])
            left_index += 1
        else:
            # Add the smaller right element to ordered_list
            ordered_list.append(right_list[right_index])
            right_index += 1

    # Add any remaining elements to ordered_list
    if right_index < len(right_list):
        ordered_list += right_list[right_index:]
    elif left_index < len(left_list):
        ordered_list += left_list[left_index:]

    return ordered_list
