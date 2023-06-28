#!/usr/bin/python3
"""Square class to represent a square"""


class Square:
    """Square class with size, position, area, and printing"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance

        Args:
            size (int): The size of the square (default 0)
            position (tuple): The position of the square (default (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): The position value to set

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers
            ValueError: If the position contains non-positive values
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
