#!/usr/bin/python3
"""Definition of an inherited list class MyList."""


class MyList(list):
    """This implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
