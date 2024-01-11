#!/usr/bin/env python3

"""Module defining type-annotated function."""

from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes string and int or float and returns a tuple."""
    return k, v * v
