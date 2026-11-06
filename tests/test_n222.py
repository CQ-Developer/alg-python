from pytest import fixture

from src.n222 import Solution, SolutionA, SolutionB, SolutionC, SolutionD, TreeNode


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC, SolutionD])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert 6 == solution.count_nodes(root)


def test_2(solution: Solution):
    assert 0 == solution.count_nodes(None)


def test_3(solution: Solution):
    root = TreeNode(1)
    assert 1 == solution.count_nodes(root)
