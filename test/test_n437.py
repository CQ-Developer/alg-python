from pytest import fixture

from src.n437 import Solution, SolutionA, TreeNode


@fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    root = TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(3),
                TreeNode(-2),
            ),
            TreeNode(
                2,
                None,
                TreeNode(1),
            ),
        ),
        TreeNode(
            -3,
            None,
            TreeNode(11),
        ),
    )
    assert 3 == solution.path_sum(root, 8)


def test_2(solution: Solution):
    root = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2),
            ),
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(
                4,
                TreeNode(5),
                TreeNode(1),
            ),
        ),
    )
    assert 3 == solution.path_sum(root, 22)
