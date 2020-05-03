"""Stack

This module implements the stack data structure.

Classes:
    Stack: Implementation of the stack data structure.
"""
from typing import Any

class Stack:
    """Implements the properties and methods required for a stack.

    Attributes:
        elements (list):
            Elements in the data structure, where the
            start of the list is the bottom and the
            end of the list is the top.
    """
    def __init__(self) -> None:
        """Sets up the stack data structure."""
        self.elements = []

    def is_empty(self) -> bool:
        """Returns whether the stack is empty.

        Returns:
            bool: True if elements is empty, False if otherwise.
        """
        return len(self.elements) == 0

    def push(self, element: Any) -> None:
        """Adds an element to the end of the stack.

        Attributes:
            element (any): The value to add.
        """
        self.elements.append(element)

    def pop(self) -> Any:
        """Removes an element from the end of the stack.

        Returns:
            any: The element that was removed.
        """
        return self.elements.pop()

    def peek(self) -> Any:
        """Returns the value of the end element in the stack.

        Returns:
            any: The value of the end element.
        """
        return self.elements[-1]

    def size(self):
        """Returns the number of elements in the stack.

        Returns:
            int: Number of elements.
        """
        return len(self.elements)
