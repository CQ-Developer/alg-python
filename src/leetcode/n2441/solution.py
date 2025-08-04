from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_max_k(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_max_k(self, nums: list[int]) -> int:
        s = set()
        res = -1
        for x in nums:
            if -x in s:
                res = max(res, abs(x))
            s.add(x)
        return res
