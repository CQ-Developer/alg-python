import pytest

from src.n85 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximal_rectangle(solution: Solution, case: Case):
    assert solution.maximal_rectangle(case["matrix"]) == case["expected"]
