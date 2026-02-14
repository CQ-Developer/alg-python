from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def shifting_letters(self, s: str, shifts: list[int]) -> str:
        pass


class SolutionA(Solution):

    @override
    def shifting_letters(self, s: str, shifts: list[int]) -> str:
        ans = []
        p = 0
        for c, x in zip(reversed(s), reversed(shifts)):
            p += x
            ans.append(chr((ord(c) - 97 + p) % 26 + 97))
        return "".join(reversed(ans))


class SolutionB(Solution):

    @override
    def shifting_letters(self, s: str, shifts: list[int]) -> str:
        suf = list(accumulate(reversed(shifts)))
        return "".join(chr((ord(c) - 97 + x) % 26 + 97) for c, x in zip(s, reversed(suf)))
