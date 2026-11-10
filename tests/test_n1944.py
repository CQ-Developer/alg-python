import pytest

from src.n1944 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_can_see_persons_count(solution: Solution, case: Case):
    assert solution.can_see_persons_count(case["heights"]) == case["expected"]
