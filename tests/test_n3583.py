import pytest

from src.n3583 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_special_triplets(solution: Solution, case: Case):
    assert solution.special_triplets(case["nums"]) == case["expected"]
