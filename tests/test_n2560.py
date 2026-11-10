import pytest

from src.n2560 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_min_capability(solution: Solution, case: Case):
    assert solution.minCapability(case["nums"], case["k"]) == case["expected"]
