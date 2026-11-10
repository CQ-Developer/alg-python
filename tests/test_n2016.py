import pytest

from src.n2016 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximum_difference(solution: Solution, case: Case):
    assert solution.maximum_difference(case["nums"]) == case["expected"]
