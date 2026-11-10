import pytest

from src.n74 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_search_matrix(solution: Solution, case: Case):
    assert solution.search_matrix(case["matrix"], case["target"]) == case["expected"]
