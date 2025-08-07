from abc import ABC, abstractmethod
from math import inf
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximum_sum(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_sum(self, nums: list[int]) -> int:
        res = -1
        tab = [-inf] * 90
        for num in nums:
            i = sum(map(int, str(num)))
            res = max(res, tab[i] + num)
            tab[i] = max(tab[i], num)
        return res
