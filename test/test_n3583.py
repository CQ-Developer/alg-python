from pytest import fixture

from src.n3583 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 1 == solution.special_triplets([6, 3, 6])


def test_b(solution: Solution):
    assert 1 == solution.special_triplets([0, 1, 0, 0])


def test_c(solution: Solution):
    assert 2 == solution.special_triplets([8, 4, 2, 8, 4])
