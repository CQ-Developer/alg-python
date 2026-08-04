from abc import ABC, abstractmethod
from collections import defaultdict
from itertools import combinations, groupby
from typing import override


class Solution(ABC):
    @abstractmethod
    def longest_balanced(self, s: str) -> int:
        pass


class SolutionA(Solution):
    @override
    def longest_balanced(self, s: str) -> int:
        # 1 letter
        ans = max(len(list(g)) for _, g in groupby(s))

        # 2 letters
        for x, y in combinations('abc', 2):
            p, pos = 0, {0: -1}
            for i, c in enumerate(s):
                if c == x or c == y:
                    p += 1 if c == x else -1
                    if p in pos:
                        ans = max(ans, i - pos[p])
                    else:
                        pos[p] = i
                else:
                    p, pos = 0, {0: i}

        # 3 letters
        pos = {(0, 0): -1}
        cnt = defaultdict(int)
        for i, c in enumerate(s):
            cnt[c] += 1
            p = (cnt['a'] - cnt['b'], cnt['b'] - cnt['c'])
            if p in pos:
                ans = max(ans, i - pos[p])
            else:
                pos[p] = i

        return ans


class SolutionB(Solution):
    @override
    def longest_balanced(self, s: str) -> int:
        n = len(s)

        # 1 letter
        def longest_1(s: str) -> int:
            ans = i = 0
            while i < n:
                j = i
                i += 1
                while i < n and s[i] == s[i - 1]:
                    i += 1
                ans = max(ans, i - j)
            return ans

        # 2 letters
        def longest_2(a: str, b: str) -> int:
            ans = i = 0
            while i < n:
                p, pos = 0, {0: i - 1}
                while i < n and (s[i] == a or s[i] == b):
                    p += 1 if s[i] == a else -1
                    if p in pos:
                        ans = max(ans, i - pos[p])
                    else:
                        pos[p] = i
                    i += 1
                i += 1
            return ans

        # 3 letters
        def longest_3(s: str) -> int:
            ans = 0
            cnt = defaultdict(int)
            pos = {(0, 0): -1}
            for i, c in enumerate(s):
                cnt[c] += 1
                p = (cnt['a'] - cnt['b'], cnt['b'] - cnt['c'])
                if p in pos:
                    ans = max(ans, i - pos[p])
                else:
                    pos[p] = i
            return ans

        return max(
            longest_1(s),
            longest_2('a', 'b'),
            longest_2('a', 'c'),
            longest_2('b', 'c'),
            longest_3(s),
        )
