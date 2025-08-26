from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def final_prices(self, prices: list[int]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def final_prices(self, prices: list[int]) -> list[int]:
        for i, x in enumerate(prices):
            for y in prices[i + 1 :]:
                if x >= y:
                    prices[i] -= y
                    break
        return prices


class SolutionB(Solution):

    @override
    def final_prices(self, prices: list[int]) -> list[int]:
        stk = [0]
        for i in range(len(prices) - 1, -1, -1):
            x = prices[i]
            while len(stk) > 1 and x < stk[-1]:
                stk.pop()
            prices[i] -= stk[-1]
            stk.append(x)
        return prices
