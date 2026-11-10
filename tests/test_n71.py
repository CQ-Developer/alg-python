import pytest

from src.n71 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_simplify_path(solution: Solution, case: Case):
    assert solution.simplify_path(case["path"]) == case["expected"]
