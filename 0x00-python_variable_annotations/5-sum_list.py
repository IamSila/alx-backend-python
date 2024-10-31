#!/usr/bin/env python3
from typing import List

"""Write a type-annotated function sum_list which
takes a list input_list of floats
as argument and returns their sum as a float."""


def sum_list(input_list: List[float]) -> float:
    """calculates the sum of values inside a list of values"""
    sum = 0

    for value in input_list:
        sum += value
    return sum
