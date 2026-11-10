import pytest

from src.n1019 import ListNode, Solution, SolutionA
from tests.case_loader import Case, load_cases
from tests.serde import build_list


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_next_larger_nodes(solution: Solution, case: Case):
    head = build_list(ListNode, case["head"])
    assert solution.next_larger_nodes(head) == case["expected"]
