from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def simplify_path(self, path: str) -> str:
        pass


class SolutionA(Solution):

    @override
    def simplify_path(self, path: str) -> str:
        stk = []
        for p in path.split('/'):
            if p == '' or p == '.':
                continue
            if p != '..':
                stk.append(p)
            elif stk:
                stk.pop()
        return '/' + '/'.join(stk)
