from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def max_profit(self, prices: list[int], strategy: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_profit(self, prices: list[int], strategy: list[int], k: int) -> int:
        s = list(accumulate((p * s for p, s in zip(prices, strategy)), initial=0))
        p = list(accumulate(prices, initial=0))
        n = len(prices)
        mx = max(s[i - k] + s[n] - s[i] + p[i] - p[i - k // 2] for i in range(k, n + 1))
        return max(s[n], mx)


class SolutionB(Solution):

    @override
    def max_profit(self, prices: list[int], strategy: list[int], k: int) -> int:
        total = s = sx = 0
        for i, (p, g) in enumerate(zip(prices, strategy)):
            total += p * g
            s += p * (1 - g)
            if i < k - 1:
                if i >= k // 2 - 1:
                    s -= prices[i - k // 2 + 1]
                continue
            sx = max(sx, s)
            s -= prices[i - k // 2 + 1] - prices[i - k + 1] * strategy[i - k + 1]
        return total + sx
