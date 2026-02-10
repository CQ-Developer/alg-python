from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_square(self, matrix: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def find_square(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        left, up = [[0] * (n + 1) for _ in range(n + 1)], [[0] * (n + 1) for _ in range(n + 1)]
        r = c = size = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 0:
                    left[i][j] = left[i][j - 1] + 1
                    up[i][j] = up[i - 1][j] + 1
                    k = min(left[i][j], up[i][j])
                    while left[i - k + 1][j] < k or up[i][j - k + 1] < k:
                        k -= 1
                    if k > size:
                        r, c, size = i - k, j - k, k
        return [r, c, size] if size else []
