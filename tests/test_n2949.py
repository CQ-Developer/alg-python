import pytest

from src.n2949 import Solution, SolutionA, SolutionB, SolutionC, SolutionD
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC, SolutionD])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_beautiful_substrings(solution: Solution, case: Case):
    assert solution.beautiful_substrings(case["s"], case["k"]) == case["expected"]
