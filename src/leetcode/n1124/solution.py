from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def longest_WPI(self, hours: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        n = len(hours)
        p, s = [0] * (n + 1), [0]
        for i, h in enumerate(hours, 1):
            p[i] = p[i - 1] + (1 if h > 8 else -1)
            if p[i] < p[s[-1]]:
                s.append(i)
        ans = 0
        for i in range(n, 0, -1):
            while s and p[i] > p[s[-1]]:
                ans = max(ans, i - s.pop())
        return ans


class SolutionB(Solution):

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        pos = [0] * (len(hours) + 2)
        ans = s = 0
        for i, h in enumerate(hours, 1):
            s -= 1 if h > 8 else -1
            if s < 0:
                ans = i
            else:
                if pos[s + 1]:
                    ans = max(ans, i - pos[s + 1])
                if pos[s] == 0:
                    pos[s] = i
        return ans
