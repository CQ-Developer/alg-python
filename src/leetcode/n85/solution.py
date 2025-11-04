from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximal_rectangle(self, matrix: list[list[str]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximal_rectangle(self, matrix: list[list[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * n

        def find_max_rec() -> int:
            mx = 0
            for i, h in enumerate(heights):
                l = i - 1
                while l >= 0 and heights[l] >= h:
                    l -= 1
                r = i + 1
                while r < n and heights[r] >= h:
                    r += 1
                mx = max(mx, h * (r - l - 1))
            return mx

        mx = 0
        for row in matrix:
            for i, x in enumerate(row):
                if x == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            mx = max(mx, find_max_rec())
        return mx
