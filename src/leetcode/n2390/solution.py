from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def remove_stars(self, s: str) -> str:
        pass


class SolutionA(Solution):

    @override
    def remove_stars(self, s: str) -> str:
        a = []
        for x in s:
            if x == '*':
                a.pop()
            else:
                a.append(x)
        return ''.join(a)
