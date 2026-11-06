import pytest
from pytest import fixture

from src.n50 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 1024.0 == pytest.approx(solution.my_pow(2.0, 10), abs=1e-05)


def test_b(solution: Solution):
    assert 9.261 == pytest.approx(solution.my_pow(2.1, 3), abs=1e-05)


def test_c(solution: Solution):
    assert 0.25 == pytest.approx(solution.my_pow(2.0, -2), abs=1e-05)
