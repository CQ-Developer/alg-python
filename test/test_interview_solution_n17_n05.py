from pytest import fixture

from src.solution_interview_n17_n05 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert ['A', '1', 'B', 'C', 'D', '2', '3', '4', 'E', '5', 'F', 'G', '6', '7'] == solution.find_longest_subarray(
        ['A', '1', 'B', 'C', 'D', '2', '3', '4', 'E', '5', 'F', 'G', '6', '7', 'H', 'I', 'J', 'K', 'L', 'M']
    )


def test_b(solution: Solution):
    assert [] == solution.find_longest_subarray(['A', 'A'])
