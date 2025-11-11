from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_squares(self, matrix: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_squares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cnt = 0
        for top in range(m):
            height = [0] * n
            for i in range(top, m):
                p, h = -1, i - top + 1
                for j in range(n):
                    height[j] += matrix[i][j]
                    if height[j] != h:
                        p = j
                    elif j - p >= h:
                        cnt += 1
        return cnt


class SolutionB(Solution):

    @override
    def count_squares(self, matrix: list[list[int]]) -> int:
        ans = 0
        height = [0] * (len(matrix[0]) + 1)

        def _count() -> int:
            cnt = 0
            stk = [-1]
            for r, hr in enumerate(height):
                while len(stk) > 1 and height[stk[-1]] >= hr:
                    h = height[stk.pop()]
                    l = stk[-1]
                    w = r - l - 1
                    up = min(h, w)
                    low = (hr if l < 0 else max(hr, height[l])) + 1
                    if low <= up:
                        cnt += (w * 2 + 2 - low - up) * (up - low + 1) // 2
                stk.append(r)
            return cnt

        for row in matrix:
            for j, x in enumerate(row):
                if x:
                    height[j] += 1
                else:
                    height[j] = 0
            ans += _count()
        return ans


class SolutionC(Solution):

    @override
    def count_squares(self, matrix: list[list[int]]) -> int:
        cnt = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    cnt += dp[i + 1][j + 1]
        return cnt


class SolutionD(Solution):

    @override
    def count_squares(self, matrix: list[list[int]]) -> int:
        cnt = 0
        dp = [0] * (len(matrix[0]) + 1)
        for row in matrix:
            p = 0
            for j, x in enumerate(row):
                t = dp[j + 1]
                dp[j + 1] = min(p, dp[j], dp[j + 1]) + 1 if x else 0
                cnt += dp[j + 1]
                p = t
        return cnt
