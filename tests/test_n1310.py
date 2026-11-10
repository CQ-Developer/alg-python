import pytest

from src.n1310 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_xor_queries(solution: Solution, case: Case):
    assert solution.xor_queries(case["arr"], case["queries"]) == case["expected"]
