#!/usr/bin/python3
"""Definition of an object attribute lookup function."""


def lookup(obj):
    """This  will return a list of an object's available attributes."""
    return (dir(obj))
