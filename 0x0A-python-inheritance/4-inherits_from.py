#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """Determines if an object is a true subclass of a class."""

    return False if type(obj) is a_class else isinstance(obj, a_class)
