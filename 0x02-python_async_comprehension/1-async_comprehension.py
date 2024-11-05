#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
write a coroutine called async_comprehension that takes no arguments. 
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    return [num async for num in async_generator()]
