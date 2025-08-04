from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_max_k(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_max_k(self, nums: list[int]) -> int:
        s = set()
        res = -1
        for x in nums:
            if -x in s:
                res = max(res, abs(x))
            s.add(x)
        return res


class SolutionB(Solution):

    @override
    def find_max_k(self, nums: list[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r and nums[l] < 0 < nums[r]:
            if -nums[l] < nums[r]:
                r -= 1
            elif -nums[l] > nums[r]:
                l += 1
            else:
                return nums[r]
        return -1
