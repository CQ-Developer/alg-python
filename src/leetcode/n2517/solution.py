from typing import override
from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maximumTastiness(self, price: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximumTastiness(self, price: list[int], k: int):
        def check(m: int) -> bool:
            pre, cnt = -m, 0
            for p in price:
                if p - pre >= m:
                    cnt += 1
                    pre = p
            return cnt >= k

        price.sort()
        l, r = 0, price[-1] - price[0]
        while l <= r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return r
