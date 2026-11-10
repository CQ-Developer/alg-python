import pytest

from src.n2818 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximum_score(solution: Solution, case: Case):
    assert solution.maximum_score(case["nums"], case["k"]) == case["expected"]
