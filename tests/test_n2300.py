import pytest

from src.n2300 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_successful_pairs(solution: Solution, case: Case):
    assert solution.successful_pairs(case["spells"], case["potions"], case["success"]) == case["expected"]
