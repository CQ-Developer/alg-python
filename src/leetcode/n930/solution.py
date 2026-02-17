from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        ans = pre = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[pre] += 1
            pre += x
            ans += cnt[pre - goal]
        return ans


class SolutionB(Solution):

    @override
    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        cnt = 0
        l1 = l2 = s1 = s2 = 0
        for r, x in enumerate(nums):
            # s2 <= goal
            s2 += x
            while l2 <= r and s2 > goal:
                s2 -= nums[l2]
                l2 += 1
            # s1  < goal
            s1 += x
            while l1 <= r and s1 >= goal:
                s1 -= nums[l1]
                l1 += 1
            cnt += l1 - l2
        return cnt
