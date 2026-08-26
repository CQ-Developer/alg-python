import unittest

from src.n2064 import Solution


def test_1():
    solution = Solution()
    assert 3 == solution.minimizedMaximum(6, [11, 6])


def test_2():
    solution = Solution()
    assert 5 == solution.minimizedMaximum(7, [15, 10, 10])


def test_3():
    solution = Solution()
    assert 100000 == solution.minimizedMaximum(1, [100000])
