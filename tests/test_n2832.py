import pytest

from src.n2832 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximum_length_of_ranges(solution: Solution, case: Case):
    assert solution.maximum_length_of_ranges(case["nums"]) == case["expected"]
