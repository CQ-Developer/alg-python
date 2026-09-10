from abc import ABC, abstractmethod
from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def ways_to_split(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和 + 二分
    """

    @override
    def ways_to_split(self, nums: list[int]) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = 0
        for r in range(2, n):
            if 3 * s[r] > 2 * s[n]:
                break
            i = bisect_left(s, 2 * s[r] - s[n], 1, r)
            j = bisect_right(s, s[r] // 2, i, r)
            ans += j - i
        return ans % 1_000_000_007


class SolutionB(Solution):
    """
    前缀和 + 滑窗
    """

    @override
    def ways_to_split(self, nums: list[int]) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = 0
        l1 = l2 = 1
        for r in range(2, n):
            while l1 < r and s[l1] <= s[r] - s[l1]:
                l1 += 1
            while l2 < l1 and s[l2] - s[r] < s[r] - s[n]:
                l2 += 1
            ans += l1 - l2
        return ans % 1_000_000_007
