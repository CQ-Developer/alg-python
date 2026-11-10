import pytest

from src.n1744 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_can_eat(solution: Solution, case: Case):
    assert solution.can_eat(case["candies_count"], case["queries"]) == case["expected"]
