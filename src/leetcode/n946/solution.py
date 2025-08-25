from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def validate_stack_sequences(self, pushed: list[int], popped: list[int]) -> bool:
        pass


class SolutionA(Solution):

    @override
    def validate_stack_sequences(self, pushed: list[int], popped: list[int]) -> bool:
        i = 0
        s = []
        for x in pushed:
            s.append(x)
            while s and s[-1] == popped[i]:
                s.pop()
                i += 1
        return len(s) == 0
