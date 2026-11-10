import pytest

from src.n363 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_sum_submatrix(solution: Solution, case: Case):
    assert solution.max_sum_submatrix(case["matrix"], case["k"]) == case["expected"]
