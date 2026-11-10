import pytest

from src.n3212 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_number_of_submatrices(solution: Solution, case: Case):
    assert solution.number_of_submatrices(case["grid"]) == case["expected"]
