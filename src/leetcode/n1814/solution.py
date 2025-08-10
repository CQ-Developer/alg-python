from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def count_nice_pairs(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_nice_pairs(self, nums: list[int]) -> int:
        res = 0
        tab = defaultdict(int)
        for num in nums:
            rev, x = 0, num
            while x > 0:
                rev *= 10
                rev += x % 10
                x //= 10
            k = num - rev
            res += tab[k]
            tab[k] += 1
        return res % 1000000007
