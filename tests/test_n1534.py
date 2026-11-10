import pytest

from src.n1534 import Solution, SolutionA, SolutionB, SolutionC
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_good_triplets(solution: Solution, case: Case):
    assert solution.count_good_triplets(case["arr"], case["a"], case["b"], case["c"]) == case["expected"]
