from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def pour_water(self, heights: list[int], volume: int, k: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def pour_water(self, heights: list[int], volume: int, k: int) -> list[int]:
        n = len(heights)
        for _ in range(volume):
            for d in -1, 1:
                j = i = k
                while 0 <= i + d < n and heights[i + d] <= heights[i]:
                    if heights[i + d] < heights[i]:
                        j = i + d
                    i += d
                if j != k:
                    heights[j] += 1
                    break
            else:
                heights[k] += 1
        return heights
