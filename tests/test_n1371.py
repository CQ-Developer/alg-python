import pytest

from src.n1371 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_the_longest_substring(solution: Solution, case: Case):
    assert solution.find_the_longest_substring(case["s"]) == case["expected"]
