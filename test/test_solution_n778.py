from pytest import fixture

from src.solution_n778 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.swimInWater([[0, 2], [1, 3]])


def test_2(solution: Solution):
    assert 16 == solution.swimInWater(
        [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    )


def test_3(solution: Solution):
    assert 11 == solution.swimInWater([[11, 15, 3, 2], [6, 4, 0, 13], [5, 8, 9, 10], [1, 14, 12, 7]])
