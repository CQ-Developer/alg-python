import pytest

from src.n2104 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_sub_array_ranges(solution: Solution, case: Case):
    assert solution.sub_array_ranges(case["nums"]) == case["expected"]
