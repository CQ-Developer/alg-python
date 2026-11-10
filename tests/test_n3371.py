import pytest

from src.n3371 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_get_largest_outlier(solution: Solution, case: Case):
    assert solution.get_largest_outlier(case["nums"]) == case["expected"]
