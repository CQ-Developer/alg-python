from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def preimageSizeFZF(self, k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def preimageSizeFZF(self, k: int) -> int:
        l, r = 0, 5 * k
        while l <= r:
            mid = (l + r) // 2
            n, cnt = 5, 0
            while n <= mid:
                cnt += mid // n
                n *= 5
            if cnt == k:
                return 5
            if cnt < k:
                l = mid + 1
            else:
                r = mid - 1
        return 0
