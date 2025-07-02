from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def peak_index_in_mountain_array(self, arr: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def peak_index_in_mountain_array(self, arr: list[int]) -> int:
        return bisect_left(range(len(arr) - 1), True, key=lambda i: arr[i] > arr[i + 1])
