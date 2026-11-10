import pytest

from src.tianchi2022_ev2bru_q3 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_arrange_bookshelf(solution: Solution, case: Case):
    assert solution.arrange_bookshelf(case["order"], case["limit"]) == case["expected"]
