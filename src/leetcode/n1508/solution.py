import heapq
from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        h: list[tuple[int, int]] = []
        for i, x in enumerate(nums):
            heapq.heappush(h, (x, i))
        s = 0
        for j in range(1, right + 1):
            x, i = heapq.heappop(h)
            if j >= left:
                s += x
            if i + 1 < n:
                heapq.heappush(h, (x + nums[i + 1], i + 1))
        return s % 1000000007
