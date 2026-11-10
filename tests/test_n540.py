import pytest

from src.n540 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_single_non_duplicate(solution: Solution, case: Case):
    assert solution.single_non_duplicate(case["nums"]) == case["expected"]
