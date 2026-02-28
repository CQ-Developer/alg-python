from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def count_subarrays(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

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
