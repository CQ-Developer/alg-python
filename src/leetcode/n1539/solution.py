from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_kth_positive(self, arr: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_kth_positive(self, arr: list[int], k: int) -> int:
        i, n, num = 0, len(arr), 1
        while k > 0:
            if i < n and arr[i] == num:
                i += 1
            else:
                k -= 1
            num += 1
        return num - 1


class SolutionB(Solution):

    @override
    def find_kth_positive(self, arr: list[int], k: int) -> int:
        def check(target: int) -> int:
            l, r = -1, len(arr)
            while l + 1 < r:
                i = (l + r) // 2
                if arr[i] >= target:
                    r = i
                else:
                    l = i
            return r

        l, r = 0, arr[-1] + k
        while l + 1 < r:
            num = (l + r) // 2
            if num - check(num + 1) >= k:
                r = num
            else:
                l = num
        return r
