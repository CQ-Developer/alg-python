from unittest.mock import patch

import pytest

from src.n278 import Solution, SolutionA, SolutionB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_first_bad_version(solution: Solution, case: Case):
    with patch("src.n278.is_bad_version", side_effect=lambda version: version >= case["bad"]):
        assert solution.first_bad_version(case["n"]) == case["expected"]
