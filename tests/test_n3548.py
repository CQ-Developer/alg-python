import pytest

from src.n3548 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_can_partition_grid(solution: Solution, case: Case):
    assert solution.can_partition_grid(case["grid"]) == case["expected"]
