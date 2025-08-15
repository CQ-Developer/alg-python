from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def number_of_subsequences(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def number_of_subsequences(self, nums: list[int]) -> int:
        res = 0
        cnt = defaultdict(int)
        for i in range(4, len(nums) - 2):
            b = nums[i - 2]
            for a in nums[: i - 3]:
                cnt[a / b] += 1
            c = nums[i]
            for d in nums[i + 2 :]:
                res += cnt[d / c]
        return res
