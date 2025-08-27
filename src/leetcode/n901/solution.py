from abc import ABC, abstractmethod
from typing import override
from math import inf


class StockSpanner(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def next(self, price: int) -> int:
        pass


class StockSpannerA(StockSpanner):

    def __init__(self):
        super().__init__()
        self.day = -1
        self.stk = [(-1, inf)]

    @override
    def next(self, price: int) -> int:
        while price >= self.stk[-1][1]:
            self.stk.pop()
        self.day += 1
        self.stk.append((self.day, price))
        return self.day - self.stk[-2][0]
