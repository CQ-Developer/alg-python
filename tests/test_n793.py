import pytest

from src.n793 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_preimage_size_f_z_f(solution: Solution, case: Case):
    assert solution.preimageSizeFZF(case["k"]) == case["expected"]
