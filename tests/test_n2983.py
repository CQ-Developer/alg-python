import pytest

from src.n2983 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_can_make_palindrome_queries(solution: Solution, case: Case):
    assert solution.can_make_palindrome_queries(case["s"], case["queries"]) == case["expected"]
