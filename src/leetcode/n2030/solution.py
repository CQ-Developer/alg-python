from abc import ABC, abstractmethod
from typing import override
from collections import Counter


class Solution(ABC):

    @abstractmethod
    def smallest_subsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        pass


class SolutionA(Solution):

    @override
    def smallest_subsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        en, n = 0, len(s)
        st, cnt = [], s.count(letter)
        for i, x in enumerate(s):
            while st and st[-1] > x and len(st) + n - i > k and (st[-1] != letter or en + cnt > repetition) or en + k - len(st) < repetition:
                if st.pop() == letter:
                    en -= 1
            if len(st) < k:
                st.append(x)
                if x == letter:
                    en += 1
            if x == letter:
                cnt -= 1
        return ''.join(st)
