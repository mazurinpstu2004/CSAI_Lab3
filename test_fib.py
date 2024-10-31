import lib
import pytest

class TestFibonacci:

    def test_positive_fibonacci(self):
        assert lib.fibonacci(5).tolist() == [0, 1, 1, 2, 3]

    def test_negative_fibonacci(self):
        with pytest.raises(ValueError):
            lib.fibonacci(0)