import pytest

from src.n2439 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_minimize_array_value(solution: Solution, case: Case):
    assert solution.minimizeArrayValue(case["nums"]) == case["expected"]
