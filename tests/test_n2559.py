import pytest

from src.n2559 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_vowel_strings(solution: Solution, case: Case):
    assert solution.vowel_strings(case["words"], case["queries"]) == case["expected"]
