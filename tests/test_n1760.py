import pytest

from src.n1760 import Solution
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[Solution])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimum_size(solution: Solution, case: Case):
    assert solution.minimumSize(case["nums"], case["maxOperations"]) == case["expected"]
