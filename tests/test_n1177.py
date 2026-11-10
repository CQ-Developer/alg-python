import pytest

from src.n1177 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_can_make_pali_queries(solution: Solution, case: Case):
    assert solution.can_make_pali_queries(case["s"], case["queries"]) == case["expected"]
