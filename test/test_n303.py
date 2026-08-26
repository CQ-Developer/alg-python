from src.n303 import NumArray


def test_a():
    code = NumArray([-2, 0, 3, -5, 2, -1])
    assert 1 == code.sum_range(0, 2)
    assert -1 == code.sum_range(2, 5)
    assert -3 == code.sum_range(0, 5)
