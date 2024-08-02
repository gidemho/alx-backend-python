#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and float numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and float numbers.

    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and float to sum.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
