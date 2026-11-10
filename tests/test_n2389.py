import pytest

from src.n2389 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_answer_queries(solution: Solution, case: Case):
    assert solution.answer_queries(case["nums"], case["queries"]) == case["expected"]
