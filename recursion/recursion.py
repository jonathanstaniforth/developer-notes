"""Recursion

This module implements a recursive function.

Functions:
    reverse_string: Reverses a list of characters.
"""
from typing import List

def reverse_string(word: List[str], start_pointer: int = 0, end_pointer: int = None) -> List:
    """Reverses a list of characters in a recursive manner.

    Attributes:
        start_pointer (int, optional): Index with the starting character. Defaults to 0.
        end_pointer (int, optional): Index with the ending character. Defaults to None.
        word (list): A list of characters.

    Returns:
        list: List of reversed characters.
    """
    if not end_pointer:
        end_pointer = len(word) - 1

    # Base case
    if start_pointer >= end_pointer:
        return None

    # Recursive case
    reverse_string(word, start_pointer + 1, end_pointer - 1)

    # Swap elements
    word[start_pointer], word[end_pointer] = word[end_pointer], word[start_pointer]

    return word
