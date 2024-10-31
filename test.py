import lib
import pytest

def test_positive_fibonacci():
        assert lib.fibonacci(5).tolist() == [0, 1, 1, 2, 3]

def test_negative_fibonacci():
        with pytest.raises(ValueError):
            lib.fibonacci(0)

def test_positive_bubble_sort():
        assert lib.bubble_sort([1, 9, 5, 3]) == [1, 3, 5, 9]

def test_negative_bubble_sort():
        with pytest.raises(ValueError):
            lib.bubble_sort([])

@pytest.fixture
def correct_example():
    return 2, 4, '*'

@pytest.fixture
def bad_operator_example():
    return 8, 4, ';'

@pytest.fixture
def divide_by_zero_example():
    return 12, 0, '/'

def test_positive_calc(correct_example):
    assert lib.calculator(*correct_example) == 8

def test_bad_operator_calc(bad_operator_example):
    with pytest.raises(ValueError):
        lib.calculator(*bad_operator_example)

def test_zero_divide_calc(divide_by_zero_example):
    with pytest.raises(ZeroDivisionError):
        lib.calculator(*divide_by_zero_example)