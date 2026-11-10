import pytest

from src.n1504 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_num_submat(solution: Solution, case: Case):
    assert solution.num_submat(case["mat"]) == case["expected"]
