import heapq
from abc import ABC, abstractmethod
from typing import override
from itertools import islice


class Solution(ABC):

    @abstractmethod
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        h = [(x + nums2[0], i, 0) for i, x in enumerate(islice(nums1, k))]
        res: list[list[int]] = []
        while len(res) < k:
            _, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
