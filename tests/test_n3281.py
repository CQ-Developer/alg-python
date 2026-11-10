import pytest

from src.n3281 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_possible_score(solution: Solution, case: Case):
    assert solution.maxPossibleScore(case["start"], case["d"]) == case["expected"]
