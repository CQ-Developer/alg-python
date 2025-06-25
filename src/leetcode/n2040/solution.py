from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def kth_smallest_product(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pass
