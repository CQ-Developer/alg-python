from abc import ABC, abstractmethod
from math import inf
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
        return nums[n // 2] if n % 2 else (nums[n // 2 - 1] + nums[n // 2]) / 2


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
        return nums[k] if len(nums) % 2 else (nums[k - 1] + nums[k]) / 2


class SolutionC(Solution):

    @override
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        l, r = -1, m
        while l + 1 < r:
            i = (l + r) // 2
            j = (m + n - 3) // 2 - i
            if nums1[i] <= nums2[j + 1]:
                l = i
            else:
                r = i
        i, j = l, (m + n - 3) // 2 - l
        ai, bj = nums1[i] if i >= 0 else -inf, nums2[j] if j >= 0 else -inf
        ai1, bj1 = nums1[i + 1] if i + 1 < m else inf, nums2[j + 1] if j + 1 < n else inf
        max1, min2 = max(ai, bj), min(ai1, bj1)
        return max1 if (m + n) % 2 else (max1 + min2) / 2
