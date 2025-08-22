from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def build_array(self, target: list[int], n: int) -> list[str]:
        pass


class SolutionA(Solution):

    @override
    def build_array(self, target: list[int], n: int) -> list[str]:
        p = 0
        seq = []
        for x in target:
            while p < x - 1:
                seq += ['Push', 'Pop']
                p += 1
            seq.append('Push')
            p = x
        return seq
