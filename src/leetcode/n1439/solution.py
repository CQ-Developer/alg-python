from abc import ABC, abstractmethod
from typing import override
from itertools import islice


class Solution(ABC):

    @abstractmethod
    def kth_smallest(self, mat: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def kth_smallest(self, mat: list[list[int]], k: int) -> int:
        res = mat[0][:k]
        for row in islice(mat, 1, None):
            res = sorted(x + y for x in res for y in row)[:k]
        return res[-1]
