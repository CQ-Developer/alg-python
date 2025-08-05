from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def max_profit(self, prices: list[int]) -> int:
        pass
