from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        pre_sum = list(accumulate(stations, initial=0))
        powers = [pre_sum[min(n, i + r + 1)] - pre_sum[max(0, i - r)] for i in range(n)]

        def check(minPower: int) -> bool:
            dif_sum = need = 0
            dif = [0] * (n + 1)
            for i in range(n):
                dif_sum += dif[i]
                m = minPower - dif_sum - powers[i]
                if m > 0:
                    need += m
                    if need > k:
                        return False
                    dif_sum += m
                    if i + 2 * r + 1 < n:
                        dif[i + 2 * r + 1] -= m
            return True

        mn = min(powers)
        left, right = mn, mn + k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
