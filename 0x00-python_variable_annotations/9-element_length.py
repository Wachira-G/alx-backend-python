#!/usr/bin/env python3

"""Module to annotate a function's parameters.
In Python, Iterable and Sequence are two different abstract base classes
that can be used as type hints.

An Iterable is any object that defines the __iter__() method
or the __getitem__() method. This means that an Iterable can be iterated over
using a for loop or the iter() function.
Examples of iterables include lists, tuples, sets, and dictionaries.

A Sequence is a more specific type of iterable that has a defined order
and can be indexed using integers.
In addition to the __iter__() and __getitem__() methods,
a Sequence also defines the __len__() method.
Examples of sequences include lists, tuples, and strings.

In the element_length() function below,
the lst parameter is annotated as an Iterable[Sequence].
This means that the function expects an iterable object
where each item is a sequence.
The function then returns a list of tuples
where each tuple contains an item from the input iterable
object and the length of that item.

By specifying both Iterable and Sequence in the type hint,
we are indicating that the input object should be iterable
and that each item in the iterable should be a sequence."""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples,
    where each tuple contains an item from the input iterable object
    and the length of that item.

    Args:
        lst: An iterable object.

    Returns:
        A list of tuples,
        where each tuple contains an item from the input iterable object
        and the length of that item.
    """
    return [(i, len(i)) for i in lst]
