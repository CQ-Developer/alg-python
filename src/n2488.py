from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override


class Solution(ABC):
    """
    求中位数为k的子数组数量
    """

    @abstractmethod
    def count_subarrays(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和 (hash表)
    """

    @override
    def count_subarrays(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = ans = 0
        no_k = True
        for x in nums:
            if x == k:
                no_k = False
            elif x > k:
                pre += 1
            else:
                pre -= 1
            if no_k:
                cnt[pre] += 1
            else:
                ans += cnt[pre] + cnt[pre - 1]
        return ans


class SolutionB(Solution):
    """
    前缀和 (数组)
    """

    @override
    def count_subarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * (n * 2)
        cnt[n] = 1
        pre, ans, not_found = n, 0, True
        for x in nums:
            if x == k:
                not_found = False
            elif x > k:
                pre += 1
            else:
                pre -= 1
            if not_found:
                cnt[pre] += 1
            else:
                ans += cnt[pre] + cnt[pre - 1]
        return ans
