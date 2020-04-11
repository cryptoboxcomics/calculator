import pytest
import calculator

def test_add():
    assert calculator.add(1, 1) == 2
def test_subtract():
    assert calculator.subtract(5, 1) == 4
def test_multiply():
    assert calculator.multiply(3, 3) == 9
def test_divide():
    assert calculator.divide(9, 3) == 3
def test_squared():
    assert calculator.squared(2) == 4