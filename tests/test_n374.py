from unittest.mock import patch

import pytest

from src.n374 import Solution, SolutionA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_guess_number(solution: Solution, case: Case):
    pick = case["pick"]

    def guess(num: int) -> int:
        if num > pick:
            return -1
        if num < pick:
            return 1
        return 0

    with patch("src.n374.guess", side_effect=guess):
        assert solution.guess_number(case["n"]) == case["expected"]
