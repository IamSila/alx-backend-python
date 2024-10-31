#!/usr/bin/env python3
from typing import List, Union

"""
Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    param mxd_list: takes in a list of ints and floats
    return: the sum as a float value
    """
    return float(sum(mxd_lst))
