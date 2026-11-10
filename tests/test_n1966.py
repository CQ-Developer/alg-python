import pytest

from src.n1966 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_binary_searchable_numbers(solution: Solution, case: Case):
    assert solution.binary_searchable_numbers(case["nums"]) == case["expected"]
