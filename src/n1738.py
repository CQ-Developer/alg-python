from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def kth_largest_value(self, matrix: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def kth_largest_value(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] ^ s[i][j + 1] ^ s[i][j] ^ x
        return sorted(x for row in s[1:] for x in row[1:])[-k]


class SolutionB(Solution):
    @override
    def kth_largest_value(self, matrix: list[list[int]], k: int) -> int:
        a = []
        col_sum = [0] * len(matrix[0])
        for row in matrix:
            s = 0
            for j, x in enumerate(row):
                col_sum[j] ^= x
                s ^= col_sum[j]
                a.append(s)
        a.sort()
        return a[-k]
