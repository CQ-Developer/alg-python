import pytest

from src.n768 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_max_chunks_to_sorted(solution: Solution, case: Case):
    assert solution.max_chunks_to_sorted(case["arr"]) == case["expected"]
