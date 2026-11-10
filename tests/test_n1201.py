import pytest

from src.n1201 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_nth_ugly_number(solution: Solution, case: Case):
    assert solution.nthUglyNumber(case["n"], case["a"], case["b"], case["c"]) == case["expected"]
