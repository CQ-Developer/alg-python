from pytest import fixture

from src.n3455 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 8 == solution.shortest_matching_substring('abaacbaecebce', 'ba*c*ce')


def test_b(solution: Solution):
    assert -1 == solution.shortest_matching_substring('baccbaadbc', 'cc*baa*adb')


def test_c(solution: Solution):
    assert 0 == solution.shortest_matching_substring('a', '**')


def test_d(solution: Solution):
    assert 6 == solution.shortest_matching_substring('madlogic', '*adlogi*')
