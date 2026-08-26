from abc import ABC, abstractmethod
from collections import defaultdict
from math import comb
from typing import override


class Solution(ABC):
    @abstractmethod
    def count_bad_pairs(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    @override
    def count_bad_pairs(self, nums: list[int]) -> int:
        res = comb(len(nums), 2)
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            res -= cnt[x - i]
            cnt[x - i] += 1
        return res
