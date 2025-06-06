# test_calculator.py
import pytest
from calculator import add, subtract

class TestCalculator:
    """Test class for calculator functions."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    def test_subtract(self):
        """Test subtraction."""
        assert subtract(10, 5) == 5
        assert subtract(0, 5) == -5
        assert subtract(-2, -3) == 1

@pytest.fixture
def sample_numbers():
    """Fixture that provides sample numbers for testing."""
    return {"a": 10, "b": 5}