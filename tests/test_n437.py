import pytest

from src.n437 import Solution, SolutionA, TreeNode
from tests.case_loader import Case, load_cases
from tests.serde import build_tree


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_path_sum(solution: Solution, case: Case):
    root = build_tree(TreeNode, case["root"])
    assert solution.path_sum(root, case["target_sum"]) == case["expected"]
