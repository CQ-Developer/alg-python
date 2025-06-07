from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(x: int) -> bool:
            cnt = 0
            for i in range(1, m + 1):
                cnt += min((x // i), n)
            return cnt >= k

        l, r = 0, m * n
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid
        return r
