from abc import ABC, abstractmethod
from collections import defaultdict
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def count_interesting_subarrays(self, nums: list[int], m: int, k: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def count_interesting_subarrays(self, nums: list[int], m: int, k: int) -> int:
        cnt = defaultdict(int)
        cnt[k] = 1
        ans = pre = 0
        for x in nums:
            if x % m == k:
                pre += 1
            ans += cnt[pre % m]
            cnt[(pre + k) % m] += 1
        return ans


class SolutionB(Solution):
    @override
    def count_interesting_subarrays(self, nums: list[int], m: int, k: int) -> int:
        cnt = [0] * min(len(nums) + 1, m)
        cnt[0] = 1
        ans = pre = 0
        for x in nums:
            if x % m == k:
                pre += 1
            if pre >= k:
                ans += cnt[(pre - k) % m]
            cnt[pre % m] += 1
        return ans


class SolutionC(Solution):
    @override
    def count_interesting_subarrays(self, nums: list[int], m: int, k: int) -> int:
        pre = list(accumulate((x % m == k for x in nums), initial=0))
        cnt = [0] * min(len(pre), m)
        ans = 0
        for s in pre:
            if s >= k:
                ans += cnt[(s - k) % m]
            cnt[s % m] += 1
        return ans
