import pytest

from src.n3542 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_min_operations(solution: Solution, case: Case):
    assert solution.min_operations(case["nums"]) == case["expected"]
