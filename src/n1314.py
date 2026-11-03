from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def matrix_block_sum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        pass


class SolutionA(Solution):
    @override
    def matrix_block_sum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        # 计算二维前缀和
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        # 计算矩形元素和
        for i in range(m):
            for j in range(n):
                i1, j1 = max(0, i - k), max(0, j - k)
                i2, j2 = min(m - 1, i + k), min(n - 1, j + k)
                mat[i][j] = s[i2 + 1][j2 + 1] - s[i2 + 1][j1] - s[i1][j2 + 1] + s[i1][j1]
        return mat
