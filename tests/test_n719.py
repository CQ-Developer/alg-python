import pytest

from src.n719 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_smallest_distance_pair(solution: Solution, case: Case):
    assert solution.smallestDistancePair(case["nums"], case["k"]) == case["expected"]
