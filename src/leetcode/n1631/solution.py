from abc import ABC, abstractmethod
from typing import override
from collections import deque


class Solution(ABC):

    @abstractmethod
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        pass


class SolutionA(Solution):
    """
    binary search
    deep first search
    """

    @override
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        vi = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int, mx: int, v: int) -> bool:
            if i == m - 1 and j == n - 1:
                return True
            vi[i][j] = v
            if i + 1 < m and vi[i + 1][j] != v and abs(heights[i][j] - heights[i + 1][j]) <= mx and dfs(i + 1, j, mx, v):
                return True
            if i >= 1 and vi[i - 1][j] != v and abs(heights[i][j] - heights[i - 1][j]) <= mx and dfs(i - 1, j, mx, v):
                return True
            if j + 1 < n and vi[i][j + 1] != v and abs(heights[i][j] - heights[i][j + 1]) <= mx and dfs(i, j + 1, mx, v):
                return True
            if j >= 1 and vi[i][j - 1] != v and abs(heights[i][j] - heights[i][j - 1]) <= mx and dfs(i, j - 1, mx, v):
                return True
            return False

        t, l, r = 0, 0, 10**6
        while l < r:
            mid = (l + r) // 2
            t += 1
            if dfs(0, 0, mid, t):
                r = mid
            else:
                l = mid + 1
        return r


class SolutionB(Solution):
    """
    binary search
    bread first search
    """

    @override
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        l, r = 0, 10**6
        while l < r:
            mid = (l + r) // 2
            vis = {(0, 0)}
            que = deque([(0, 0)])
            while que:
                i, j = que.popleft()
                for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in vis and abs(heights[i][j] - heights[x][y]) <= mid:
                        que.append((x, y))
                        vis.add((x, y))
            if (m - 1, n - 1) in vis:
                r = mid
            else:
                l = mid + 1
        return r
