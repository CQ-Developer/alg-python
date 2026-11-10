import pytest

from src.n316 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_remove_duplicate_letters(solution: Solution, case: Case):
    assert solution.remove_duplicate_letters(case["s"]) == case["expected"]
