import pytest

from src.n84 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_largest_rectangle_area(solution: Solution, case: Case):
    assert solution.largest_rectangle_area(case["heights"]) == case["expected"]
