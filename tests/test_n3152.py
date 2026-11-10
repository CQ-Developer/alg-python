import pytest

from src.n3152 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_is_array_special(solution: Solution, case: Case):
    assert solution.is_array_special(case["nums"], case["queries"]) == case["expected"]
