import pytest

from src.n2513 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimize_set(solution: Solution, case: Case):
    assert (
        solution.minimizeSet(case["divisor1"], case["divisor2"], case["uniqueCnt1"], case["uniqueCnt2"])
        == case["expected"]
    )
