#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second
"""

import asyncio
import random
from typing import Generator

async def async_generator():
    number = random.randint(0, 10)
    for i in range(10):
        asyncio.sleep(1)
        yield number
