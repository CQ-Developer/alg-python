import pytest

from src.n162 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_peak_element(solution: Solution, case: Case):
    result = solution.find_peak_element(case["nums"])
    if "expected_any" in case:
        assert result in case["expected_any"]
    else:
        assert result == case["expected"]
