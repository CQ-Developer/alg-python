from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def min_subarray(self, nums: list[int], p: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def min_subarray(self, nums: list[int], p: int) -> int:
        pre = list(accumulate(nums, initial=0))
        x = pre[-1] % p
        ans = n = len(nums)
        last = {}
        for i, v in enumerate(pre):
            last[v % p] = i
            j = last.get((v - x) % p, -n)
            ans = min(ans, i - j)
        return ans if ans < n else -1


class SolutionB(Solution):
    @override
    def min_subarray(self, nums: list[int], p: int) -> int:
        x = sum(nums) % p
        s = 0
        ans = n = len(nums)
        last = {0: -1}
        for i, v in enumerate(nums):
            s += v
            last[s % p] = i
            j = last.get((s - x) % p, -n)
            ans = min(ans, i - j)
        return ans if ans < n else -1
