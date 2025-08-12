from abc import ABC, abstractmethod
from math import gcd
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_beautiful_pairs(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_beautiful_pairs(self, nums: list[int]) -> int:
        res = 0
        cnt = [0] * 10
        for x in nums:
            for i in range(1, 10):
                if cnt[i] and gcd(i, x % 10) == 1:
                    res += cnt[i]
            while x >= 10:
                x //= 10
            cnt[x] += 1
        return res
