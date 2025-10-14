from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def mct_from_leaf_values(self, arr: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    动态规划
    """

    @override
    def mct_from_leaf_values(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [[1 << 30 for _ in range(n)] for _ in range(n)]
        mx = [[0 for _ in range(n)] for _ in range(n)]
        for j, x in enumerate(arr):
            mx[j][j] = x
            dp[j][j] = 0
            for i in range(j - 1, -1, -1):
                mx[i][j] = max(arr[i], mx[i + 1][j])
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + mx[i][k] * mx[k + 1][j])
        return dp[0][n - 1]


class SolutionB(Solution):
    """
    单调栈
    """

    @override
    def mct_from_leaf_values(self, arr: list[int]) -> int:
        s = 0
        stk = []
        for x in arr:
            while stk and x >= stk[-1]:
                y = stk.pop()
                if not stk or stk[-1] > x:
                    s += y * x
                else:
                    s += y * stk[-1]
            stk.append(x)
        while len(stk) > 1:
            x = stk.pop()
            s += stk[-1] * x
        return s


class SolutionC(Solution):
    """
    贪心
    """

    @override
    def mct_from_leaf_values(self, arr: list[int]) -> int:
        s = 0
        while len(arr) > 1:
            j, mn = -1, 1 << 30
            for i in range(len(arr) - 1):
                if arr[i] * arr[i + 1] < mn:
                    mn = arr[i] * arr[i + 1]
                    j = i if arr[i] < arr[i + 1] else i + 1
            s += mn
            del arr[j]
        return s
