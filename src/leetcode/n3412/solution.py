from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def calculate_score(self, s: str) -> int:
        pass


class SolutionA(Solution):

    @override
    def calculate_score(self, s: str) -> int:
        score = 0
        table = [[] for _ in range(26)]
        for i, c in enumerate(map(ord, s)):
            c -= 97
            if table[25 - c]:
                score += i - table[25 - c].pop()
            else:
                table[c].append(i)
        return score
