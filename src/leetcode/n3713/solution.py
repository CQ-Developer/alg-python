from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def longest_balanced(self, s: str) -> int:
        pass


class SolutionA(Solution):

    @override
    def longest_balanced(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            mx, cnt = 0, defaultdict(int)
            for j, x in enumerate(s[i:], i):
                cnt[x] += 1
                mx = max(mx, cnt[x])
                if mx * len(cnt) == j - i + 1:
                    ans = max(ans, j - i + 1)
        return ans
