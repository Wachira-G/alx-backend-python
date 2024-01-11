#!/usr/bin/env python3

"""Module with type annotations."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Takes three paratmetesrs and retuuns the item in dict at key or None."""
    if key in dct:
        return dct[key]
    else:
        return default
