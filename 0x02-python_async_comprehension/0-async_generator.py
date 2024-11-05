#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[int, None, None]:
    """generates a random float number in the given range"""
    for i in range(0, 10, 1):
        await asyncio.sleep(1)
        yield random.random() * 10
