from abc import ABC, abstractmethod
from typing import override
from collections import Counter, defaultdict


class Solution(ABC):

    @abstractmethod
    def arrange_bookshelf(self, order: list[int], limit: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def arrange_bookshelf(self, order: list[int], limit: int) -> list[int]:
        st = []
        en, re = defaultdict(int), Counter(order)
        for x in order:
            re[x] -= 1
            if en[x] == limit:
                continue
            while st and x < st[-1] and en[st[-1]] + re[st[-1]] > limit:
                en[st.pop()] -= 1
            st.append(x)
            en[x] += 1
        return st
