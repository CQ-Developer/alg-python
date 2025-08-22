from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def backspace_compare(self, s: str, t: str) -> bool:
        pass


class SolutionA(Solution):

    @override
    def backspace_compare(self, s: str, t: str) -> bool:
        a = b = ''
        for c in s:
            if c == '#':
                a = a[:-1]
            else:
                a += c
        for c in t:
            if c == '#':
                b = b[:-1]
            else:
                b += c
        return a == b


class SolutionB(Solution):

    @override
    def backspace_compare(self, s: str, t: str) -> bool:
        sk1 = sk2 = 0
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    sk1 += 1
                    i -= 1
                elif sk1 > 0:
                    sk1 -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    sk2 += 1
                    j -= 1
                elif sk2 > 0:
                    sk2 -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True
