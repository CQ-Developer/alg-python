from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class MountainArray(ABC):

    @abstractmethod
    def get(self, index: int) -> int:
        pass

    @abstractmethod
    def length(self) -> int:
        pass


class Solution(ABC):

    @abstractmethod
    def find_in_mountain_array(self, target: int, mountainArr: MountainArray) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_in_mountain_array(self, target: int, mountainArr: MountainArray) -> int:
        def search(x: int, l: int, r: int, f: bool) -> int:
            while l <= r:
                i = (l + r) // 2
                y = mountainArr.get(i)
                if f:
                    y = -y
                if y == x:
                    return i
                if y > x:
                    r = i - 1
                else:
                    l = i + 1
            return -1

        n = mountainArr.length()
        j = bisect_left(range(n - 1), True, key=lambda i: mountainArr.get(i) > mountainArr.get(i + 1))
        i = search(target, 0, j, False)
        if i == -1:
            i = search(-target, j + 1, n - 1, True)
        return i
