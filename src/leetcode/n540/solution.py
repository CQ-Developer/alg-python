from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def single_non_duplicate(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def single_non_duplicate(self, nums: list[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
        return result


class SolutionB(Solution):

    @override
    def single_non_duplicate(self, nums: list[int]) -> int:
        l, r = -1, len(nums) // 2
        while l + 1 < r:
            i = (l + r) // 2
            if nums[i * 2] != nums[i * 2 + 1]:
                r = i
            else:
                l = i
        return nums[r * 2]


class SolutionC(Solution):

    @override
    def single_non_duplicate(self, nums: list[int]) -> int:
        check = lambda k: nums[k * 2] != nums[k * 2 + 1]
        i = bisect_left(range(len(nums) // 2), True, key=check)
        return nums[i * 2]
