import pytest

from src.n3067 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_count_pairs_of_connectable_servers(solution: Solution, case: Case):
    assert solution.count_pairs_of_connectable_servers(case["edges"], case["signalSpeed"]) == case["expected"]
