#!/usr/bin/python3

"""Augment module's code."""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the sequence if it is not empty,
    otherwise return None.

    Args:
        lst: A sequence of any type of elements.

    Returns:
        The first element of the sequence if it is not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
