#!/usr/bin/python3

"""Module for summation of list with members as floats and ints."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Take a list of floats and ints and give their sum."""
    return sum(mxd_lst)
