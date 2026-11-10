import pytest

from src.n3404 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_number_of_subsequences(solution: Solution, case: Case):
    assert solution.number_of_subsequences(case["nums"]) == case["expected"]
