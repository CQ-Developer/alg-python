from abc import ABC, abstractmethod
from math import inf
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_profit(self, prices: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_profit(self, prices: list[int]) -> int:
        buy, profit = inf, 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
