import pytest

from src.n2711 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_difference_of_distinct_values(solution: Solution, case: Case):
    assert solution.difference_of_distinct_values(case["grid"]) == case["expected"]
