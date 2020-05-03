"""Deque

This module implements the deque data structure.

Classes:
    Deque: Implementation of the deque data structure.
"""
from typing import Any

class Deque:
    """Implements the properties and methods required for a deque.

    Attributes:
        elements (list):
            Elements in the data structure, where the
            start of the list is the end and the end
            of the list is the front.
    """
    def __init__(self) -> None:
        """Sets up the deque data structure."""
        self.elements = []

    def is_empty(self) -> bool:
        """Returns whether the deque is empty.

        Returns:
            bool: True if elements is empty, False otherwise.
        """
        return len(self.elements) == 0

    def add_front(self, element: Any) -> None:
        """Adds an element to the right side of the deque.

        Args:
            element (any): The value to add.
        """
        self.elements.append(element)

    def add_rear(self, element: Any) -> None:
        """Adds an element to the left side of the deque.

        Args:
            element (any): The value to add.
        """
        self.elements.insert(0, element)

    def remove_front(self) -> Any:
        """Removes an element from the right side of the deque.

        Returns:
            any: The element that was removed.
        """
        return self.elements.pop()

    def remove_rear(self) -> Any:
        """Removes an element from the left side of the deque.

        Returns:
            any: The element that was removed.
        """
        return self.elements.pop(0)

    def size(self) -> int:
        """Returns the number of elements in the deque.

        Returns:
            int: Number of elements.
        """
        return len(self.elements)
