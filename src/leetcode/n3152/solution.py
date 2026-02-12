from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate, pairwise


class Solution(ABC):

    @abstractmethod
    def is_array_special(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        pass


class SolutionA(Solution):

    @override
    def is_array_special(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """
        p = [0]
        for a, b in pairwise(nums):
            p.append(p[-1] + (a % 2 == b % 2))
        """
        p = list(accumulate((a % 2 == b % 2 for a, b in pairwise(nums)), initial=0))
        return [p[a] == p[b] for a, b in queries]


class SolutionB(Solution):

    @override
    def is_array_special(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """
        dp = [1]
        for a, b in pairwise(nums):
            if a % 2 != b % 2:
                dp.append(dp[-1] + 1)
            else:
                dp.append(1)
        """
        dp = list(accumulate(pairwise(nums), lambda acc, x: 1 if x[0] % 2 == x[1] % 2 else acc + 1, initial=1))
        return [b - a + 1 <= dp[b] for a, b in queries]
