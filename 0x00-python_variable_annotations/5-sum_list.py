#!/usr/bin/env python3

"""Module for type-annotated function with list."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Take list of floats and return their sum."""
    return sum(input_list)
