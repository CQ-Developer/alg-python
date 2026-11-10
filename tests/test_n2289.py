import pytest

from src.n2289 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_total_steps(solution: Solution, case: Case):
    assert solution.total_steps(case["nums"]) == case["expected"]
