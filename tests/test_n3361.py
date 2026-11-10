import pytest

from src.n3361 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_shift_distance(solution: Solution, case: Case):
    assert solution.shift_distance(case["s"], case["t"], case["next_cost"], case["previous_cost"]) == case["expected"]
