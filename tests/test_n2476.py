from pytest import fixture

from src.n2476 import Solution, SolutionA, TreeNode


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    root = TreeNode(
        6, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(13, TreeNode(9), TreeNode(15, TreeNode(14), None))
    )
    assert [[2, 2], [4, 6], [15, -1]] == solution.closest_nodes(root, [2, 5, 16])


def test_2(solution: Solution):
    root = TreeNode(4, None, TreeNode(9))
    assert [[-1, 4]] == solution.closest_nodes(root, [3])
