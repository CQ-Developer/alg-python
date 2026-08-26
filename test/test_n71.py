from pytest import fixture

from src.n71 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert '/home' == solution.simplify_path('/home/')
