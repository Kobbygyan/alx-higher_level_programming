#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class with its size and proper validation"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
