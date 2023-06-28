#!/usr/bin/python3
"""Class representing a Square"""


class Square():
    """Square class with size and area calculation"""

    def __init__(self, size=0):
        """Initialize the Square instance

        Args:
            size (int): The size of the square (default 0)
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
