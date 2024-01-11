#!/usr/bin/env python3

"""Module for type annotated function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes arg and retuns function that multiplies a float by multiplier."""

    def callback(x: float) -> float:
        """returns product of two floats."""
        return multiplier * x

    return callback
