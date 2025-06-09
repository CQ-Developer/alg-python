from abc import ABC, abstractmethod
from typing import override
from itertools import chain
from sortedcontainers import SortedList


class Solution(ABC):

    @abstractmethod
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        arr = SortedList(chain.from_iterable(matrix))
        return arr[k - 1]
