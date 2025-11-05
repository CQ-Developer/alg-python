from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximal_square(self, matrix: list[list[str]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximal_square(self, matrix: list[list[str]]) -> int:
        n = len(matrix[0])
        h = [0] * n

        def find() -> int:
            mx = 0
            for i, x in enumerate(h):
                l = i - 1
                while l >= 0 and h[l] >= x:
                    l -= 1
                r = i + 1
                while r < n and h[r] >= x:
                    r += 1
                mx = max(mx, min(x, r - l - 1))
            return mx

        s = 0
        for row in matrix:
            for j, x in enumerate(row):
                if x == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            s = max(s, find())
        return s * s


class SolutionB(Solution):

    @override
    def maximal_square(self, matrix: list[list[str]]) -> int:
        s = 0
        m, n = len(matrix), len(matrix[0])
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == '1':
                    f[i + 1][j + 1] = min(f[i][j], f[i + 1][j], f[i][j + 1]) + 1
                    s = max(s, f[i + 1][j + 1])
        return s * s


class SolutionC(Solution):

    @override
    def maximal_square(self, matrix: list[list[str]]) -> int:
        s = 0
        n = len(matrix[0])
        f = [0] * (n + 1)
        for row in matrix:
            p = 0
            for j, x in enumerate(row):
                if x == '1':
                    t = f[j + 1]
                    f[j + 1] = min(p, f[j], f[j + 1]) + 1
                    s = max(s, f[j + 1])
                    p = t
                else:
                    f[j + 1] = p = 0
        return s * s
