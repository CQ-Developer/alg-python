from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def max_sum_min_product(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_sum_min_product(self, nums: list[int]) -> int:
        ans = 0
        stk = [-1]
        pre = [0] + [x for x in accumulate(nums)]
        for r, x in enumerate(nums + [-1]):
            while len(stk) > 1 and nums[stk[-1]] > x:
                y = nums[stk.pop()]
                l = stk[-1]
                ans = max(ans, y * (pre[r] - pre[l + 1]))
            stk.append(r)
        return ans % (10**9 + 7)
