from abc import ABC, abstractmethod
from typing import override
from collections import Counter


class Solution(ABC):

    @abstractmethod
    def smallest_subsequence(self, s: str) -> str:
        pass


class SolutionA(Solution):

    @override
    def smallest_subsequence(self, s: str) -> str:
        st = []
        re, en = Counter(s), set()
        for x in s:
            re[x] -= 1
            if x in en:
                continue
            while st and x < st[-1] and re[st[-1]]:
                y = st.pop()
                en.remove(y)
            st.append(x)
            en.add(x)
        return ''.join(st)
