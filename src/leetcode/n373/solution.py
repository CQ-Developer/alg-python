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


class SolutionB(Solution):

    @override
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        m, n = len(nums1), len(nums2)
        hp = [(nums1[0] + nums2[0], 0, 0)]
        res: list[list[int]] = []
        while len(res) < k:
            _, i, j = heapq.heappop(hp)
            res.append([nums1[i], nums2[j]])
            if j == 0 and i + 1 < m:
                heapq.heappush(hp, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < n:
                heapq.heappush(hp, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
