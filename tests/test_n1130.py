import pytest

from src.n1130 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_mct_from_leaf_values(solution: Solution, case: Case):
    assert solution.mct_from_leaf_values(case["arr"]) == case["expected"]
