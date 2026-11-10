import pytest

from src.n2968 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_frequency_score(solution: Solution, case: Case):
    assert solution.max_frequency_score(case["nums"], case["k"]) == case["expected"]
