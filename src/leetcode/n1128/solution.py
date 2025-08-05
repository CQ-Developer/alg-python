from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def num_equiv_domino_pairs(self, dominoes: list[list[int]]) -> int:
        pass
