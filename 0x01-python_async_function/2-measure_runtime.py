#!/usr/bin/env python3


"""Module to measuere the runtime."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Runs wait_n function, measures its runtime then
    return the total execution time."""
    loop = asyncio.get_event_loop()

    start = time.time()
    loop.run_until_complete(wait_n(n, max_delay))
    end = time.time()
    loop.close()
    total_execution_time = end - start
    return total_execution_time / n
