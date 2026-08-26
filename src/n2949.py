from abc import ABC, abstractmethod
from collections import Counter
from itertools import count
from typing import override


class Solution(ABC):
    """
    设子串长度为 L
    那么需要满足: L² % 4k = 0
    """

    @abstractmethod
    def beautiful_substrings(self, s: str, k: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def beautiful_substrings(self, s: str, k: int) -> int:
        for i in count(1):
            if (i * i) % (4 * k) == 0:
                k = i
                break
        pre = [0]
        for c in s:
            x = 1 if c in "aeiou" else -1
            pre.append(x + pre[-1])
        ans = 0
        cnt = Counter()
        for i, x in enumerate(pre):
            p = (i % k, x)
            ans += cnt[p]
            cnt[p] += 1
        return ans


class SolutionB(Solution):
    @override
    def beautiful_substrings(self, s: str, k: int) -> int:
        for d in count(1):
            if (d * d) % (4 * k) == 0:
                k = d
                break
        cnt = Counter([(k - 1, 0)])
        ans = pre = 0
        for i, c in enumerate(s):
            pre += 1 if c in "aeiou" else -1
            p = (i % k, pre)
            ans += cnt[p]
            cnt[p] += 1
        return ans


class SolutionC(Solution):
    @override
    def beautiful_substrings(self, s: str, k: int) -> int:
        k = self._sqrt(4 * k)
        cnt = Counter([(k - 1, 0)])
        ans = pre = 0
        for i, c in enumerate(s):
            pre += 1 if c in "aeiou" else -1
            p = (i % k, pre)
            ans += cnt[p]
            cnt[p] += 1
        return ans

    def _sqrt(self, n: int) -> int:
        ans = 1
        p = 2
        while p * p <= n:
            if n % p == 0:
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                ans *= p ** ((e + 1) // 2)
            p += 1
        if n > 1:
            ans *= n
        return ans


class SolutionD(Solution):
    @override
    def beautiful_substrings(self, s: str, k: int) -> int:
        _k = 1
        while (_k * _k) % k != 0:
            _k += 1
        _k *= 2
        cnt = Counter([(_k - 1, 0)])
        ans = pre = 0
        for i, c in enumerate(s):
            pre += 1 if c in "aeiou" else -1
            p = (i % _k, pre)
            ans += cnt[p]
            cnt[p] += 1
        return ans
