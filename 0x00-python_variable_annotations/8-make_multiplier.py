#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that multiplies a float by multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the multiplier.

        Parameters:
        value (float): The float value to be multiplied.

        Returns:
        float: The result of the multiplication.
        """
        return value * multiplier

    return multiplier_function
