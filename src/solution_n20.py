from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def is_valid(self, s: str) -> bool:
        pass


class SolutionA(Solution):
    @override
    def is_valid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in '([{':
                stk.append(c)
            elif c == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            elif c == ']':
                if stk and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
            elif c == '}':
                if stk and stk[-1] == '{':
                    stk.pop()
                else:
                    return False
        return not stk
