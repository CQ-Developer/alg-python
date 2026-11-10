import pytest

from src.n456 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_132_pattern(solution: Solution, case: Case):
    assert solution.find_132_pattern(case["nums"]) == case["expected"]
