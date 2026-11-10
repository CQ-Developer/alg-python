import pytest

from src.n1031 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_sum_two_no_overlap(solution: Solution, case: Case):
    assert solution.max_sum_two_no_overlap(case["nums"], case["first_len"], case["second_len"]) == case["expected"]
