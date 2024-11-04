#!/usr/bin/env python3
"""asyncio.create_tasks in action
author: Sila Mulingi
github: https://www.github.com/IamSila
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns the class of an asyncio coroutine"""
    return asyncio.create_task(
        wait_random(max_delay)
    )
