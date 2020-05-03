"""Timsort

This module implements the timsort algorithm,
including both the insertion sort and
merge sort algorithms.

Functions:
    insertion_sort: Modified version of insertion sort.
    merge_sort: Modified version of merge sort.
    timsort: Implementation of timsort.
"""
from typing import List

def insertion_sort(elements: List, left_boundary: int = 0, \
    right_boundary: int = None) -> List:
    """Sorts a list using the insertion sort algorithm.

    This version of the algorithm implements boundaries
    to sort particular areas of the list.

    Args:
        elements (list): Unordered list of elements.
        left_boundary (int, optional): Start point in elements. Defaults to 0.
        right_boundary (int, optional): End point in elements. Defaults to None.

    Returns:
        list: Ordered list of elements.
    """
    if right_boundary is None:
        right_boundary = len(elements)

    # Pass through the list of elements based on the boundaries provided.
    for element in range(left_boundary + 1, right_boundary):
        element_value = elements[element]
        pointer = element - 1

        # Compare element to ordered sublist, checking if the value of
        # element is less than or equal to the ordered elements.
        while pointer >= left_boundary and elements[pointer] > element_value:
            # Move larger valued ordered element one position to the right.
            elements[pointer + 1] = elements[pointer]
            # Move along the ordered sublist from right to left
            pointer -= 1

        # Insert element to the right of the lower valued ordered element.
        elements[pointer + 1] = element_value

    return elements

def merge_sort(left_list: List, right_list: List) -> List:
    """Sort two lists using the merge sort algorithm.

    This implementation does not split the lists,
    but, instead merges two lists together.

    Args:
        left_list (list): List of elements.
        right_list (list): List of elements.

    Returns:
        list: Ordered list of elements
    """
    # If the first array is empty, then nothing
    # needs to be merged, and you can return
    # the second array as the result.
    if len(left_list) == 0:
        return right_list

    # If the second array is empty, then nothing
    # needs to be merged, and you can return
    # the first array as the result.
    if len(right_list) == 0:
        return left_list

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

def timsort(elements: List) -> List:
    """Sorts a list using the timsort algorithm.

    This algorithm makes use of the modified insertion
    and merge sort algorithms. Insertion sort is used
    to break up the elements and merge sort is used
    to put them back together.

    Args:
        elements (list): Unordered list of elements.

    Returns:
        list: Ordered list of elements.
    """
    # run_length should be between 32 and 64
    run_length = 32
    number_elements = len(elements)

    # Slice the elements in to smaller lists, based on run_length
    for left_boundary in range(0, number_elements, run_length):
        # Prevent right_boundary going beyond the array length
        right_boundary = min((left_boundary + run_length), number_elements)
        # Sort the elements inplace
        insertion_sort(elements, left_boundary, right_boundary)

    # Loop through all the slices and merge them together
    size = run_length

    while size < number_elements:
        for start in range(0, number_elements, size * 2):
            # Calculate the slices
            midpoint = (start + size - 1) + 1
            # Prevent end being larger than number of elements
            end = min((start + size * 2 - 1), (number_elements - 1)) + 1

            # Merge the two lists
            merged_array = merge_sort(
                left_list=elements[start:midpoint],
                right_list=elements[midpoint:end])

            # Place merged slices into elements list
            elements[start:start + len(merged_array)] = merged_array

        # Each iteration doubles size
        size *= 2

    return elements
