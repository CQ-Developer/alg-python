from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def min_subarray(self, nums: list[int], p: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def min_subarray(self, nums: list[int], p: int) -> int:
        pre = list(accumulate(nums, initial=0))
        s = pre[-1]
        if s % p == 0:
            return 0
        ans = n = len(nums)
        last = defaultdict(lambda: -n)
        for i, x in enumerate(pre):
            last[(x + s) % p] = i
            ans = min(ans, i - last[x % p])
        return ans if ans < n else -1


class SolutionB(Solution):

    @override
    def min_subarray(self, nums: list[int], p: int) -> int:
        s = sum(nums) % p
        if s == 0:
            return 0
        x = 0
        ans = n = len(nums)
        last = {s: -1}
        for i, v in enumerate(nums):
            x = (x + v) % p
            last[(x + s) % p] = i
            ans = min(ans, i - last.get(x, -n))
        return ans if ans < n else -1
