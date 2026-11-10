import pytest

from src.n654 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases
from tests.serde import tree_to_list


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_construct_maximum_binary_tree(solution: Solution, case: Case):
    result = solution.construct_maximum_binary_tree(case["nums"])
    assert tree_to_list(result) == case["expected"]
