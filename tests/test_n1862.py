import pytest

from src.n1862 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_sum_of_floored_pairs(solution: Solution, case: Case):
    assert solution.sum_of_floored_pairs(case["nums"]) == case["expected"]
