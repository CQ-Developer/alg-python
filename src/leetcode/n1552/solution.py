from typing import override
from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maxDistance(self, position: list[int], m: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maxDistance(self, position: list[int], m: int) -> int:
        def check(mid: int) -> bool:
            pre, cnt = -mid, 0
            for p in position:
                if p - pre >= mid:
                    pre = p
                    cnt += 1
            return cnt >= m

        position.sort()
        l, r = 0, position[-1] - position[0]
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
