from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def max_side_length(self, mat: list[list[int]], threshold: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def max_side_length(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        ans = 0
        for i in range(m):
            for j in range(n):
                r, c = i + 1, j + 1
                while r <= m and c <= n:
                    area = s[r][c] - s[r][j] - s[i][c] + s[i][j]
                    if area > threshold:
                        break
                    ans = max(ans, r - i)
                    r += 1
                    c += 1
        return ans


class SolutionB(Solution):
    """
    思路同上，只是语法层面的优化
    """

    @override
    def max_side_length(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x

        def _query(r1: int, c1: int, r2: int, c2: int) -> int:
            return s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1]

        ans = 0
        for i in range(m):
            for j in range(n):
                while i + ans < m and j + ans < n and _query(i, j, i + ans, j + ans) <= threshold:
                    ans += 1
        return ans
