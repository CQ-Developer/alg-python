import pytest

from src.n1895 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_largest_magic_square(solution: Solution, case: Case):
    assert solution.largest_magic_square(case["grid"]) == case["expected"]
