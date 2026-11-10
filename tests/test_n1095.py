import pytest

from src.n1095 import MountainArray, Solution, SolutionA
from tests.case_loader import Case, load_cases


class FakeMountainArray(MountainArray):
    def __init__(self, arr: list[int]) -> None:
        self._arr = arr

    def get(self, index: int) -> int:
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", load_cases(__file__))
def test_find_in_mountain_array(solution: Solution, case: Case):
    mountain_array = FakeMountainArray(case["arr"])
    assert solution.find_in_mountain_array(case["target"], mountain_array) == case["expected"]
