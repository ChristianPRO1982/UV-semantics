"""Basic math utility functions."""
from typing import Union

Number = Union[int, float]

def add(num1: Number, num2: Number) -> float:
    return float(num1 + num2)
