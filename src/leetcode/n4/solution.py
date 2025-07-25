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


class SolutionB(Solution):

    @override
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = []
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        nums += nums1[i:]
        nums += nums2[j:]
        k = (m + n) // 2
        return nums[k] if len(nums) % 2 != 0 else (nums[k - 1] + nums[k]) / 2
