from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override


class Solution(ABC):

    @abstractmethod
    def pair_sums(self, nums: list[int], target: int) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def pair_sums(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        tab = defaultdict(int)
        for num in nums:
            x = target - num
            if tab[x]:
                res.append([x, num])
                tab[x] -= 1
            else:
                tab[num] += 1
        return res
