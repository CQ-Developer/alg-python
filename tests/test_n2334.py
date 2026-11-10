import pytest

from src.n2334 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_valid_subarray_size(solution: Solution, case: Case):
    result = solution.valid_subarray_size(case["nums"], case["threshold"])
    assert result in case["expected_any"]
