import pytest

from src.n2791 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_palindrome_paths(solution: Solution, case: Case):
    assert solution.count_palindrome_paths(case["parent"], case["s"]) == case["expected"]
