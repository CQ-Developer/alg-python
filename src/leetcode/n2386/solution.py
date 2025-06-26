import heapq
from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def k_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def k_sum(self, nums: list[int], k: int) -> int:
        s = 0
        for i, x in enumerate(nums):
            if x >= 0:
                s += x
            else:
                nums[i] = -x
        nums.sort()
        x, n = 0, len(nums)
        h = [(nums[0], 0)]
        for _ in range(1, k):
            x, i = heapq.heappop(h)
            if i + 1 < n:
                heapq.heappush(h, (x + nums[i + 1], i + 1))
                heapq.heappush(h, (x - nums[i] + nums[i + 1], i + 1))
        return s - x
