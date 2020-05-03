"""Linked list

This module implements the linked list data structure.

Classes:
    Node: An element in a linked list data structure.
    LinkedList: Implementation of the linked list data structure.
"""
from __future__ import annotations
from typing import Any, Union

class Node:
    """A node in a linked list that holds a
    value and a reference to the next node.

    Attributes:
        value (any): The value of the node.
        next (Node, None): The node after this node.
    """
    def __init__(self, value: Any, next_node: Node = None) -> None:
        """Set up the node.

        Args:
            value (any): The value of the node.
            next_node (Node, None, optional):
                Reference to the next node. Defaults to None.
        """
        self.value = value
        self.next = next_node

class LinkedList:
    """Implements the properties and methods required for
    a linked list.

    Attributes:
        head (Node, None): The starting node of the linked list.
        size (int): Number of nodes in the linked list.
    """
    def __init__(self):
        """Set up the linked list."""
        self.head = None
        self.size = 0

    def get(self, node_value: Any) -> Union[Node, None]:
        """Find a node with a value in the list.

        Args:
            node_value (any): Value of the node to retrieve.

        Returns:
            Node: The node with node_value.
            None: Returns when the node is not found.
        """
        node = self.head

        while node is not None:
            if node.get_value() == node_value:
                return node

            node = node.get_next()

        return None

    def is_empty(self) -> bool:
        """Returns whether the linked list is empty.

        Returns:
            bool: True if elements is empty, False if otherwise.
        """
        return self.size <= 0

    def add_at_head(self, node_value: Any) -> None:
        """Add a node to the start of the linked list.

        Args:
            node_value (any): Value of the node.
        """
        self.head = Node(node_value, self.head)
        self.size += 1

    def add_at_tail(self, node_value) -> None:
        """Add a node to the end of the linked list.

        Args:
            node_value (any): Value of the node.
        """
        if self.is_empty():
            return self.add_at_head(node_value)

        node = self.head

        while node.next is not None:
            node = node.next

        node.next = Node(node_value)
        self.size += 1

    def add_at_index(self, index: int, node_value: Any) -> None:
        """Add a node to a particular index in the linked list.

        Args:
            index (int): The position to add the node.
            node_value (any): Value of the node.
        """
        if index > self.size:
            return None

        if index == 0:
            self.add_at_head(node_value)
        else:
            node = self.head

            while (index - 1) > 0:
                node = node.next
                index -= 1

            node.next = Node(node_value, node.next)

        self.size += 1
        return None

    def remove(self, node_value: Any) -> None:
        """Remove a node with a particular value from
        the linked list.

        Args:
            node_value (any): Value of the node.
        """
        if self.is_empty():
            return None

        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.value == node_value:
                if not previous_node:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next

                self.size -= 1
                break

            previous_node = current_node
            current_node = current_node.next

    def remove_at_index(self, index: int) -> None:
        """Remove a node at a particular index from
        the linked list.

        Args:
            index (int): The position of the node to remove.
        """
        if index < 0 or index >= self.size:
            return None

        if index == 0:
            self.add_at_head(self.head.next)
        else:
            node = self.head

            while (index - 1) > 0:
                node = node.next
                index -= 1

            node.next = node.next.next

        self.size -= 1
        return None
