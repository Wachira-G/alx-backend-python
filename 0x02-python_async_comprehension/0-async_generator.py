#!/usr/bin/env python3

"""Module for an async generator."""


import asyncio
import random
from typing import AsyncGenerator


# Generator annotations take form of
# Generator[yield_type, send_type, return_type]


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times, each time waiting 1 sec yielding a random number
    between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
