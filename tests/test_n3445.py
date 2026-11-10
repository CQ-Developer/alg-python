import pytest

from src.n3445 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_difference(solution: Solution, case: Case):
    assert solution.max_difference(case["s"], case["k"]) == case["expected"]
