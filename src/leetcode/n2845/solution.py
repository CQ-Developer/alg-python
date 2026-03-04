from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def count_interesting_subarrays(self, nums: list[int], m: int, k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_interesting_subarrays(self, nums: list[int], m: int, k: int) -> int:
        cnt = defaultdict(int)
        cnt[k % m] = 1
        ans = s = 0
        for x in nums:
            if x % m == k:
                s += 1
            ans += cnt[s % m]
            cnt[(s + k) % m] += 1
        return ans


class SolutionB(Solution):

    @override
    def count_interesting_subarrays(self, nums: list[int], m: int, k: int) -> int:
        cnt = [0] * min(len(nums) + 1, m)
        cnt[0] = 1
        ans = s = 0
        for x in nums:
            if x % m == k:
                s += 1
            if s >= k:
                ans += cnt[(s - k) % m]
            cnt[s % m] += 1
        return ans
