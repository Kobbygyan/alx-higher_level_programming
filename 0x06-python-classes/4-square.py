#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square class with size, property, and area calculation"""

    def __init__(self, size=0):
        """Initialize the Square instance

        Args:
            size (int): The size of the square (default 0)
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): The size value to set

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
