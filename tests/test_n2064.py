import pytest

from src.n2064 import Solution
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[Solution])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimized_maximum(solution: Solution, case: Case):
    assert solution.minimizedMaximum(case["n"], case["quantities"]) == case["expected"]
