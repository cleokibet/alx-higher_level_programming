#!/usr/bin/python3
"""Definition a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("The size must be >= 0")
        self.__size = size

    def area(self):
        """Returning the current area of the square."""
        return (self.__size * self.__size)
