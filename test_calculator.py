import lib
import pytest

class TestCalculator:

    @pytest.fixture
    def correct_example(self):
        return 2, 4, '*'

    @pytest.fixture
    def bad_operator_example(self):
        return 8, 4, ';'

    @pytest.fixture
    def divide_by_zero_example(self):
        return 12, 0, '/'

    def test_positive_calc(self, correct_example):
        assert lib.calculator(*correct_example) == 8

    def test_bad_operator_calc(self, bad_operator_example):
        with pytest.raises(ValueError):
            lib.calculator(*bad_operator_example)

    def test_zero_divide_calc(self, divide_by_zero_example):
        with pytest.raises(ZeroDivisionError):
            lib.calculator(*divide_by_zero_example)
