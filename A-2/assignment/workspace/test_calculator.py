import pytest
from calculator import Calculator

def test_calculator():
    calculator = Calculator()
    assert calculator.add(1, 2) == 3
    assert calculator.subtract(2, 1) == 1
    assert calculator.multiply(2, 3) == 6
    assert calculator.divide(6, 2) == 3
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
