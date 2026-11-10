import pytest

from src.n1814 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_nice_pairs(solution: Solution, case: Case):
    assert solution.count_nice_pairs(case["nums"]) == case["expected"]
