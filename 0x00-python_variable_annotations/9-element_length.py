#!/usr/bin/env python3
"""
This module provides a function that returns the length of elements
in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains
    an element from the iterable and its corresponding length.

    Parameters:
    lst (Iterable[Sequence]): The iterable of sequences to process.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples,
    each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
