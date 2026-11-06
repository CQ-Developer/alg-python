import unittest

from src.n1760 import Solution


def test_1():
    solution = Solution()
    assert 3 == solution.minimumSize([9], 2)


def test_2():
    solution = Solution()
    assert 2 == solution.minimumSize([2, 4, 8, 2], 4)


def test_3():
    solution = Solution()
    assert 7 == solution.minimumSize([7, 17], 2)
