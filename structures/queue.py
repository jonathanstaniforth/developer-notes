"""Queue

This module implements the queue data structure.

Classes:
    Queue: Implementation of the queue data structure.
"""
from typing import Any

class Queue:
    """Implements the properties and methods required for a queue.

    Attributes:
        elements (list):
            Elements in the data structure, where the
            start of the list is the start and the
            end of the list is the end.
    """
    def __init__(self) -> None:
        """Sets up the queue data structure."""
        self.elements = []

    def is_empty(self) -> bool:
        """Returns whether the queue is empty.

        Returns:
            bool: True if elements is empty, False if otherwise.
        """
        return len(self.elements) == 0

    def enqueue(self, element: Any) -> None:
        """Adds an element to the start of the queue.

        Args:
            element (any): The value to add.
        """
        self.elements.insert(0, element)

    def dequeue(self) -> Any:
        """Removes an element from the end of the queue.

        Returns:
            any: The element that was removed.
        """
        return self.elements.pop()

    def size(self) -> int:
        """Returns the number of elements in the queue.

        Returns:
            int: Number of elements.
        """
        return len(self.elements)
