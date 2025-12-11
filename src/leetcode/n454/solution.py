from abc import ABC, abstractmethod
from typing import override
from collections import Counter


class Solution(ABC):

    @abstractmethod
    def four_sum_count(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def four_sum_count(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        tab = Counter(x + y for x in nums1 for y in nums2)
        return sum(tab[-x - y] for x in nums3 for y in nums4)
