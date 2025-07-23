from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        pass
