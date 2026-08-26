from pytest import fixture

from src.n1019 import ListNode, Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [5, 5, 0] == solution.next_larger_nodes(ListNode(2, ListNode(1, ListNode(5))))


def test_2(solution: Solution):
    assert [7, 0, 5, 5, 0] == solution.next_larger_nodes(
        ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))
    )
