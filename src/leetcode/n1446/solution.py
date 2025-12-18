from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_power(self, s: str) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_power(self, s: str) -> int:
        n, mx = len(s), 0
        for i in range(n):
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            mx = max(mx, j - i)
            i = j
        return mx
