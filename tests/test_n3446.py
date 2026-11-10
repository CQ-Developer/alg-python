import pytest

from src.n3446 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_sort_matrix(solution: Solution, case: Case):
    assert solution.sort_matrix(case["grid"]) == case["expected"]
