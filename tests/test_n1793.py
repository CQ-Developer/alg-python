import pytest

from src.n1793 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximum_score(solution: Solution, case: Case):
    assert solution.maximum_score(case["nums"], case["k"]) == case["expected"]
