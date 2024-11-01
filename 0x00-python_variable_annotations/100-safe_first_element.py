#!/usr/bin/env python3
"""task 10, advanced tasks"""
from typing import Union, Sequence, Any


def safe_first_elements(lst: Sequence[Any]) -> Union[Any, None]:
    """returns elements from the list if provided, otherwise, none"""
    if lst:
        return lst[0]
    else:
        return None
