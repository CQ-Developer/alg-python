import pytest

from src.n1712 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_ways_to_split(solution: Solution, case: Case):
    assert solution.ways_to_split(case["nums"]) == case["expected"]
