from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def search(self, nums: list[int], target: int) -> bool:
        pass


class SolutionA(Solution):

    @override
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return True
            if nums[l] < nums[i]:
                if nums[l] <= target < nums[i]:
                    r = i - 1
                else:
                    l = i + 1
            elif nums[l] > nums[i]:
                if nums[i] < target <= nums[r]:
                    l = i + 1
                else:
                    r = i - 1
            else:
                l += 1
        return False
