import pytest

from src.n1010 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_num_pairs_divisible_by_60(solution: Solution, case: Case):
    assert solution.num_pairs_divisible_by_60(case["time"]) == case["expected"]
