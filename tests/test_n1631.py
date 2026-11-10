import pytest

from src.n1631 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimum_effort_path(solution: Solution, case: Case):
    assert solution.minimumEffortPath(case["heights"]) == case["expected"]
