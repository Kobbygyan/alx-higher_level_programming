#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Node class for a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize the Node instance

        Args:
            data (int): The data value of the node
            next_node (Node): The next node in the linked list (default None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node

        Args:
            value (int): The data value to set

        Raises:
            TypeError: If the data is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node in the linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list

        Args:
            value (Node): The next node to set

        Raises:
            TypeError: If the next_node is not a Node object or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class"""

    def __init__(self):
        """Initialize the SinglyLinkedList instance"""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list

        Args:
            value (int): The data value of the new Node
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list"""
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
