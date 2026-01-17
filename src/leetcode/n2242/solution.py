from abc import ABC, abstractmethod
from typing import override
from heapq import nlargest


class Solution(ABC):

    @abstractmethod
    def maximum_score(self, scores: list[int], edges: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_score(self, scores: list[int], edges: list[list[int]]) -> int:
        g = [[] for _ in range(len(scores))]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        for i, v in enumerate(g):
            if len(v) > 3:
                g[i] = nlargest(3, v, key=lambda i: scores[i])
        ans = -1
        for x, y in edges:
            for a in g[x]:
                for b in g[y]:
                    if a != y and b != x and a != b:
                        ans = max(ans, scores[a] + scores[x] + scores[y] + scores[b])
        return ans
