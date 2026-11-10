import pytest

from src.n3455 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_shortest_matching_substring(solution: Solution, case: Case):
    assert solution.shortest_matching_substring(case["s"], case["p"]) == case["expected"]
