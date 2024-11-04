#!/usr/bin/env python3

"""
coroutings and asynchronous processes basic syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """a coroutines that first process the wait time
    to end then returns the waited time"""
    t = random.random() * max_delay
    await asyncio.sleep(t)
    return t
