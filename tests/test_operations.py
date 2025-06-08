import pytest
from app import addition, division, subtraction, multiplication


def test_addition():
    assert addition(1, 1) == 2


def test_subtraction():
    assert subtraction(1, 1) == 0


def test_multiplication():
    assert multiplication(1, 1) == 1


def test_division_positive():
    assert division(1, 1) == 1.0


def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        division(10, 0)
