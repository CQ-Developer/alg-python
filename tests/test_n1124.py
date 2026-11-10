import pytest

from src.n1124 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_longest_w_p_i(solution: Solution, case: Case):
    assert solution.longest_WPI(case["hours"]) == case["expected"]
