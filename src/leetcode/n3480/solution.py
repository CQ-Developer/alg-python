from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_subarrays(self, n: int, conflicting_pairs: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_subarrays(self, n: int, conflicting_pairs: list[list[int]]) -> int:
        groups = [[] for _ in range(n + 1)]
        for a, b in conflicting_pairs:
            if a > b:
                a, b = b, a
            groups[a].append(b)
        ans = 0
        extra = [0] * (n + 2)
        b = [n + 1, n + 1]
        for i in range(n, 0, -1):
            b += groups[i]
            b.sort()
            b = b[:2]
            ans += b[0] - i
            extra[b[0]] += b[1] - b[0]
        return ans + max(extra)


class SolutionB(Solution):

    @override
    def max_subarrays(self, n: int, conflicting_pairs: list[list[int]]) -> int:
        groups = [[] for _ in range(n + 1)]
        for a, b in conflicting_pairs:
            if a > b:
                a, b = b, a
            groups[a].append(b)
        cnt = mx = ex = 0
        b0 = b1 = n + 1
        for i in range(n, 0, -1):
            _b0 = b0
            for b in groups[i]:
                if b < b0:
                    b0, b1 = b, b0
                elif b < b1:
                    b1 = b
            cnt += b0 - i
            if _b0 != b0:
                ex = 0
            ex += b1 - b0
            mx = max(mx, ex)
        return cnt + mx


class SolutionC(Solution):

    @override
    def max_subarrays(self, n: int, conflicting_pairs: list[list[int]]) -> int:
        g0, g1 = [n + 1] * (n + 1), [n + 1] * (n + 1)
        for a, b in conflicting_pairs:
            if a > b:
                a, b = b, a
            if b < g0[a]:
                g0[a], g1[a] = b, g0[a]
            elif b < g1[a]:
                g1[a] = b
        ans = mx = ex = 0
        b0 = b1 = n + 1
        for i in range(n, 0, -1):
            _b0 = b0
            if g0[i] < b0:
                b0, b1 = g0[i], min(b0, g1[i])
            elif g0[i] < b1:
                b1 = g0[i]
            ans += b0 - i
            if _b0 != b0:
                ex = 0
            ex += b1 - b0
            mx = max(mx, ex)
        return ans + mx
