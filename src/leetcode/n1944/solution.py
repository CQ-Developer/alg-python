from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def can_see_persons_count(self, heights: list[int]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def can_see_persons_count(self, heights: list[int]) -> list[int]:
        n = len(heights)
        a = [0] * n
        s = []
        for i in range(n - 1, -1, -1):
            while s and heights[i] > s[-1]:
                s.pop()
                a[i] += 1
            if s:
                a[i] += 1
            s.append(heights[i])
        return a
