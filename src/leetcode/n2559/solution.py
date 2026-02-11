from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def vowel_strings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def vowel_strings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        p = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            if w[0] in "aeiou" and w[-1] in "aeiou":
                p[i + 1] = p[i] + 1
            else:
                p[i + 1] = p[i]
        return [p[r + 1] - p[l] for l, r in queries]


class SolutionB(Solution):

    @override
    def vowel_strings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        p = list(accumulate((w[0] in "aeiou" and w[-1] in "aeiou" for w in words), initial=0))
        return [p[r + 1] - p[l] for l, r in queries]
