import pytest

from src.n1539 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_kth_positive(solution: Solution, case: Case):
    assert solution.find_kth_positive(case["arr"], case["k"]) == case["expected"]
