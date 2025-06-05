# tests/test_calculator.py
from my_app.calculator import add, subtract

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_subtract_numbers():
    assert subtract(5, 2) == 3

def test_failing_example():
    # This test is intentionally set to fail, so you can see failures in TeamCity
    assert add(1, 1) == 3
