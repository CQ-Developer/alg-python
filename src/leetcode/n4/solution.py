from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        pass


class SolutionA(Solution):

    @override
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = [*nums1, *nums2]
        nums.sort()
        n = len(nums)
        return nums[n // 2] if n % 2 == 1 else (nums[n // 2 - 1] + nums[n // 2]) / 2
