#!/usr/bin/env python3

"""
coroutings and asynchronous processes basic syntax
"""
import asyncio, random

async def wait_random(max_delay: int = 10):
    """a coroutines that first process the wait time to end then returns the waited time"""
    t = random.random() * 10
    await asyncio.sleep(t)
    return t
