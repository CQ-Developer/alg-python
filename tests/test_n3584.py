import pytest

from src.n3584 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_maximum_product(solution: Solution, case: Case):
    assert solution.maximum_product(case["nums"], case["m"]) == case["expected"]
