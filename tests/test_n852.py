import pytest

from src.n852 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_peak_index_in_mountain_array(solution: Solution, case: Case):
    assert solution.peak_index_in_mountain_array(case["arr"]) == case["expected"]
