import pytest

from src.n1749 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_absolute_sum(solution: Solution, case: Case):
    assert solution.max_absolute_sum(case["nums"]) == case["expected"]
