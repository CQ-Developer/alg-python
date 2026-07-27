from pytest import fixture

from src.solution_n654 import Solution, SolutionA, SolutionB, TreeNode


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert TreeNode(
        6, TreeNode(3, right=TreeNode(2, right=TreeNode(1))), TreeNode(5, left=TreeNode(0))
    ) == solution.construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])


def test_2(solution: Solution):
    assert TreeNode(3, right=TreeNode(2, right=TreeNode(1))) == solution.construct_maximum_binary_tree([3, 2, 1])
