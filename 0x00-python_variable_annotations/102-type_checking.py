#!/usr/bin/env python3

"""This module provides a function to zoom in on an array.

The module contains a single function, `zoom_array`,
which takes a tuple and a factor as input
and returns a list with the elements of the tuple repeated by the factor.

Example usage:
    array = (12, 72, 91)
    zoom_2x = zoom_array(array)
    zoom_3x = zoom_array(array, 3)

"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in on an array.

    This function takes a tuple and a factor as input
    and returns a list with the elements of the tuple repeated by the factor.

    Args:
        lst: A tuple of elements to be zoomed in on.
        factor: An integer representing the factor by which to zoom in
        on the tuple. Default is 2.

    Returns:
        A list with the elements of the tuple repeated by the factor.

    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
