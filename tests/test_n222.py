import pytest

from src.n222 import Solution, SolutionA, SolutionB, SolutionC, SolutionD, TreeNode
from tests.case_loader import Case, load_cases
from tests.serde import build_tree


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC, SolutionD])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_nodes(solution: Solution, case: Case):
    root = build_tree(TreeNode, case["root"])
    assert solution.count_nodes(root) == case["expected"]
