import pytest

from src.n1074 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_num_submatrix_sum_target(solution: Solution, case: Case):
    assert solution.num_submatrix_sum_target(case["matrix"], case["target"]) == case["expected"]
