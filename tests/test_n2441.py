import pytest

from src.n2441 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_max_k(solution: Solution, case: Case):
    assert solution.find_max_k(case["nums"]) == case["expected"]
