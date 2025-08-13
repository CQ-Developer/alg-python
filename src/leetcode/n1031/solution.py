from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def max_sum_two_no_overlap(self, nums: list[int], first_len: int, second_len: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_sum_two_no_overlap(self, nums: list[int], first_len: int, second_len: int) -> int:
        s = list(accumulate(nums, initial=0))

        def f(a, b) -> int:
            res = mx = 0
            for i in range(a + b, len(s)):
                mx = max(mx, s[i - a] - s[i - a - b])
                res = max(res, mx + s[i] - s[i - a])
            return res

        return max(f(first_len, second_len), f(second_len, first_len))


class SolutionB(Solution):

    @override
    def max_sum_two_no_overlap(self, nums: list[int], first_len: int, second_len: int) -> int:
        s = list(accumulate(nums, initial=0))
        res = a = b = 0
        for i in range(first_len + second_len, len(s)):
            a = max(a, s[i - first_len] - s[i - first_len - second_len])
            b = max(b, s[i - second_len] - s[i - first_len - second_len])
            res = max(res, a + s[i] - s[i - first_len], b + s[i] - s[i - second_len])
        return res
