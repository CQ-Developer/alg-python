import pytest

from src.n1673 import Solution, SolutonA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutonA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_most_competitive(solution: Solution, case: Case):
    assert solution.most_competitive(case["nums"], case["k"]) == case["expected"]
