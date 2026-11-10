import pytest

from src.n1685 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_get_sum_absolute_differences(solution: Solution, case: Case):
    assert solution.get_sum_absolute_differences(case["nums"]) == case["expected"]
