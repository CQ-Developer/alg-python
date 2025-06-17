from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        pass
