import pytest

from src.n525 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_max_length(solution: Solution, case: Case):
    assert solution.find_max_length(case["nums"]) == case["expected"]
