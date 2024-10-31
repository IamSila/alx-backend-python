#!/usr/bin/env python3

"""annoting the function as requires"""
from typing import Iteratable, List, Sequence, Tuple


def element_length(lst: Iteratable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return the elements of lst, and the length of a list of sequences"""
    return [(i, len(i)) for i in lst]
