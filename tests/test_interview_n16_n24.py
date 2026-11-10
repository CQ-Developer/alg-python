import pytest

from src.interview_n16_n24 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_pair_sums(solution: Solution, case: Case):
    assert solution.pair_sums(case["nums"], case["target"]) == case["expected"]
