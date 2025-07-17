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
