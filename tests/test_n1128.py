import pytest

from src.n1128 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_num_equiv_domino_pairs(solution: Solution, case: Case):
    assert solution.num_equiv_domino_pairs(case["dominoes"]) == case["expected"]
