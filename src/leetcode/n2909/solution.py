from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def minimum_sum(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def minimum_sum(self, nums: list[int]) -> int:
        n = len(nums)

        suf = [0] * n
        suf[-1] = nums[-1]
        for j in range(n - 2, 1, -1):
            suf[j] = min(suf[j + 1], nums[j])

        ans, pre = inf, nums[0]
        for j in range(1, n - 1):
            if pre < nums[j] > suf[j + 1]:
                ans = min(ans, pre + nums[j] + suf[j + 1])
            pre = min(pre, nums[j])

        return -1 if ans is inf else int(ans)
