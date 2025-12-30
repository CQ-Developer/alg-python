from abc import ABC, abstractmethod
from typing import override
from itertools import groupby, combinations
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def longest_balanced(self, s: str) -> int:
        pass


class SolutionA(Solution):

    @override
    def longest_balanced(self, s: str) -> int:
        n = len(s)

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
