import pytest

from src.n50 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_my_pow(solution: Solution, case: Case):
    result = solution.my_pow(case["x"], case["n"])
    assert result == pytest.approx(case["expected"], abs=1e-5)
