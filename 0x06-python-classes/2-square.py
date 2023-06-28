#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Square class with its size and proper validation"""

    def __init__(self, sz=0):
        if type(sz) is not int:
            raise TypeError("sz must be an integer")
        elif sz < 0:
            raise ValueError("sz must be >= 0")
        self.__sz = sz
