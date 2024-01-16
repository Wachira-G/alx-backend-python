#!/usr/bin/env python3

"""Module to get run time for four parallel comprehensions."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime of 4 parallel async comprehensions."""
    start = time.time()
    results = await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end = time.time()
    total_time = end - start
    return total_time
