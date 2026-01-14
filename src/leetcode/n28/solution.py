from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def str_str(self, haystack: str, needle: str) -> int:
        pass


class SolutionA(Solution):

    @override
    def str_str(self, haystack: str, needle: str) -> int:
        n = len(needle)
        cnt = 0
        pi = [0] * n
        for i, s in enumerate(needle[1:], 1):
            while cnt > 0 and needle[cnt] != s:
                cnt = pi[cnt - 1]
            if needle[cnt] == s:
                cnt += 1
            pi[i] = cnt
        cnt = 0
        for i, s in enumerate(haystack):
            while cnt > 0 and needle[cnt] != s:
                cnt = pi[cnt - 1]
            if needle[cnt] == s:
                cnt += 1
            if cnt == n:
                return i - cnt + 1
        return -1
