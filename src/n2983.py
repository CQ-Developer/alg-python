from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def can_make_palindrome_queries(self, s: str, queries: list[list[int]]) -> list[bool]:
        pass


class SolutionA(Solution):
    @override
    def can_make_palindrome_queries(self, s: str, queries: list[list[int]]) -> list[bool]:
        n = len(s) // 2
        t = s[n:][::-1]
        s = s[:n]

        sum_s = [[0] * 26]
        for i, b in enumerate(s):
            sum_s.append(sum_s[-1][:])
            sum_s[-1][ord(b) - 97] += 1

        sum_t = [[0] * 26]
        for i, b in enumerate(t):
            sum_t.append(sum_t[-1][:])
            sum_t[-1][ord(b) - 97] += 1

        sum_ne = list(accumulate((x != y for x, y in zip(s, t)), initial=0))

        def count(sum: list[list[int]], l: int, r: int) -> list[int]:
            return [y - x for x, y in zip(sum[l], sum[r + 1])]

        def subtract(s1: list[int], s2: list[int]) -> list[int]:
            for i, s in enumerate(s2):
                s1[i] -= s
                if s1[i] < 0:
                    return False
            return s1

        def check(l1: int, r1: int, l2: int, r2: int, sum_s: list[list[int]], sum_t: list[list[int]]) -> bool:
            if sum_ne[l1] > 0 or sum_ne[n] - sum_ne[max(r1, r2) + 1] > 0:
                return False
            # 区间包含
            if r2 <= r1:
                return count(sum_s, l1, r1) == count(sum_t, l1, r1)
            # 区间不相交
            if r1 < l2:
                return (
                    sum_ne[l2] - sum_ne[r1 + 1] == 0
                    and count(sum_s, l1, r1) == count(sum_t, l1, r1)
                    and count(sum_s, l2, r2) == count(sum_t, l2, r2)
                )
            # 区间相交但不包含
            s1 = subtract(count(sum_s, l1, r1), count(sum_t, l1, l2 - 1))
            s2 = subtract(count(sum_t, l2, r2), count(sum_s, r1 + 1, r2))
            return s1 and s2 and s1 == s2

        ans = []
        for i, (l1, r1, c, d) in enumerate(queries):
            l2, r2 = n * 2 - 1 - d, n * 2 - 1 - c
            if l1 <= l2:
                ans.append(check(l1, r1, l2, r2, sum_s, sum_t))
            else:
                ans.append(check(l2, r2, l1, r1, sum_t, sum_s))
        return ans
