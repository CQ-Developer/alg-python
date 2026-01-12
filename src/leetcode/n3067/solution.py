from abc import ABC, abstractmethod
from typing import override
from functools import cache


class Solution(ABC):

    @abstractmethod
    def count_pairs_of_connectable_servers(self, edges: list[list[int]], signalSpeed: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def count_pairs_of_connectable_servers(self, edges: list[list[int]], signalSpeed: int) -> list[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        def dfs(x: int, f: int, s: int) -> int:
            cnt = 0 if s % signalSpeed else 1
            for y, w in g[x]:
                if y != f:
                    cnt += dfs(y, x, s + w)
            return cnt

        ans = [0] * n
        for x, gi in enumerate(g):
            if len(gi) > 1:
                s = 0
                for y, w in gi:
                    cnt = dfs(y, x, w)
                    ans[x] += cnt * s
                    s += cnt
        return ans


class SolutionB(Solution):

    @override
    def count_pairs_of_connectable_servers(self, edges: list[list[int]], signalSpeed: int) -> list[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        @cache
        def dfs(x: int, f: int, s: int) -> int:
            cnt = 0 if s else 1
            for y, w in g[x]:
                if y != f:
                    cnt += dfs(y, x, (s + w) % signalSpeed)
            return cnt

        ans = [0] * n
        for x, gi in enumerate(g):
            if len(gi) > 1:
                s = 0
                for y, w in gi:
                    cnt = dfs(y, x, w % signalSpeed)
                    ans[x] += cnt * s
                    s += cnt
        return ans
