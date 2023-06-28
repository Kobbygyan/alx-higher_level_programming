#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize a Square instance

        Args:
            size (float or int): The size of the square (default 0)
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
            value (float or int): The size value to set

        Raises:
            TypeError: If the size is not a number (float or int)
            ValueError: If the size is less than 0
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two Square instances for equality"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Compare two Square instances for inequality"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """Compare if a Square instance is greater than another"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Compare if a Square instance is greater than or equal to another"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """Compare if a Square instance is less than another"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Compare if a Square instance is less than or equal to another"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
