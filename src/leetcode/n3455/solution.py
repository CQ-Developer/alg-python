from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def shortest_matching_substring(self, s: str, p: str) -> int:
        pass


class SolutionA(Solution):

    @override
    def shortest_matching_substring(self, s: str, p: str) -> int:
        def kmp(p: str, n: int) -> list[int]:
            if not n:
                return list(range(len(s) + 1))
            cnt = 0
            pi = [0] * n
            for i, v in enumerate(p[1:], 1):
                while cnt and p[cnt] != v:
                    cnt = pi[cnt - 1]
                if p[cnt] == v:
                    cnt += 1
                pi[i] = cnt
            cnt = 0
            ans = []
            for i, v in enumerate(s):
                while cnt and p[cnt] != v:
                    cnt = pi[cnt - 1]
                if p[cnt] == v:
                    cnt += 1
                if cnt == n:
                    ans.append(i - n + 1)
                    cnt = pi[cnt - 1]
            return ans

        p1, p2, p3 = p.split("*")
        n1, n2, n3 = len(p1), len(p2), len(p3)
        pos1, pos2, pos3 = kmp(p1, n1), kmp(p2, n2), kmp(p3, n3)
        m1, m3 = len(pos1), len(pos3)

        ans = inf
        i = k = 0
        for j in pos2:
            while k < m3 and pos3[k] < j + n2:
                k += 1
            if k == m3:
                break
            while i < m1 and pos1[i] <= j - n1:
                i += 1
            if i:
                ans = min(ans, pos3[k] + n3 - pos1[i - 1])

        return -1 if ans == inf else int(ans)
