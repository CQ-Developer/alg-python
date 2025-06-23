from abc import ABC, abstractmethod
from typing import override
from math import lcm
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        n = len(coins)

        def check(x: int) -> bool:
            cnt = 0
            for s in range(1, 1 << n):
                y = 1
                for i, v in enumerate(coins):
                    if (1 << i & s) != 0:
                        y = lcm(v, y)
                        if y > x:
                            break
                else:
                    cnt += x // y if s.bit_count() & 1 else -(x // y)
            return cnt >= k

        return bisect_left(range(min(coins) * k), True, k, key=check)
