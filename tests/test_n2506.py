import pytest

from src.n2506 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_similar_pairs(solution: Solution, case: Case):
    assert solution.similar_pairs(case["words"]) == case["expected"]
