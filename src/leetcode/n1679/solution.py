from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def max_operations(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_operations(self, nums: list[int], k: int) -> int:
        res = 0
        tab = defaultdict(int)
        for num in nums:
            if tab[k - num] > 0:
                res += 1
                tab[k - num] -= 1
            else:
                tab[num] += 1
        return res
