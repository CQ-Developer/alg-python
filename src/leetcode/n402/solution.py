from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def remove_k_digits(self, num: str, k: int) -> str:
        pass


class SolutionA(Solution):

    @override
    def remove_k_digits(self, num: str, k: int) -> str:
        stk = []
        for s in num:
            while k and stk and s < stk[-1]:
                stk.pop()
                k -= 1
            stk.append(s)
        if k:
            stk = stk[:-k]
        return ''.join(stk).lstrip('0') or '0'
