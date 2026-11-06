from pytest import fixture

from src.n3067 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [0, 4, 6, 6, 4, 0] == solution.count_pairs_of_connectable_servers(
        [[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1
    )


def test_b(solution: Solution):
    assert [2, 0, 0, 0, 0, 0, 2] == solution.count_pairs_of_connectable_servers(
        [[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], 3
    )
