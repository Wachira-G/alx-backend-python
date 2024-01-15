#!/usr/bin/env python3

"""Module to execute multiple coroutines at the same time with async."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """runs wait_random n times and returns list of all the delays."""
    return sorted([await wait_random(max_delay) for i in range(n)])
