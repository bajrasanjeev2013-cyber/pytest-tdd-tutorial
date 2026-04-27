import pytest
from src.calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_add_two_positive_numbers(self, calculator):
        assert calculator.add(2, 3) == 5

    def test_add_negative_numbers(self, calculator):
        assert calculator.add(-2, -3) == -5

    def test_subtract_numbers(self, calculator):
        assert calculator.subtract(5, 3) == 2

    def test_multiply_numbers(self, calculator):
        assert calculator.multiply(4, 3) == 12

    def test_divide_numbers(self, calculator):
        assert calculator.divide(10, 2) == 5.0

    def test_divide_by_zero_raises_exception(self, calculator):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 5, 5),
        (2.5, 1.5, 4.0)
    ])
    def test_add_parametrized(self, calculator, a, b, expected):
        assert calculator.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (10, 7, 3),
        (-2, -5, 3),
        (0, 5, -5)
    ])
    def test_subtract_parametrized(self, calculator, a, b, expected):
        assert calculator.subtract(a, b) == expected