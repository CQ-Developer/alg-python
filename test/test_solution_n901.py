from pytest import fixture

from src.solution_n901 import StockSpanner, StockSpannerA


@fixture(scope='module', params=[StockSpannerA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.next(100)
    assert 1 == solution.next(80)
    assert 1 == solution.next(60)
    assert 2 == solution.next(70)
    assert 1 == solution.next(60)
    assert 4 == solution.next(75)
    assert 6 == solution.next(85)
