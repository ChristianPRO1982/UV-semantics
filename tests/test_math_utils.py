"""Tests for math utility functions."""
from di03_test_de_uv_et_semantics.math_utils import add


def test_add_two_positive_numbers():
    result = add(1, 2)
    assert result == 3.0


def test_add_with_float_values():
    result = add(1.5, 2.5)
    assert result == 4.0
    assert result == 4  # This will fail due to type mismatch
