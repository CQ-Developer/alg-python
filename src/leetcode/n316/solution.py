from abc import ABC, abstractmethod
from typing import override
from collections import Counter


class Solution(ABC):

    @abstractmethod
    def remove_duplicate_letters(self, s: str) -> str:
        pass


class SolutionA(Solution):

    @override
    def remove_duplicate_letters(self, s: str) -> str:
        left = Counter(s)
        st = []
        en = set()
        for c in s:
            left[c] -= 1
            if c in en:
                continue
            while st and c < st[-1] and left[st[-1]]:
                en.remove(st.pop())
            st.append(c)
            en.add(c)
        return ''.join(st)
