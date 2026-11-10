import pytest

from src.n1542 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_longest_awesome(solution: Solution, case: Case):
    assert solution.longest_awesome(case["s"]) == case["expected"]
