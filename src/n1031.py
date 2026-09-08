from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    """
    给你一个整数数组 nums 和两个整数 first_len 和 second_len,
    请你找出并返回两个无重叠子数组中元素的最大和, 长度分别为
    first_len 和 second_len.

    长度为 first_len 的子数组可以出现在长为 second_len 的子数组之前或之后,
    但二者必须是无重叠的.

    子数组是数组的一个连续部分.
    """

    @abstractmethod
    def max_sum_two_no_overlap(self, nums: list[int], first_len: int, second_len: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def max_sum_two_no_overlap(self, nums: list[int], first_len: int, second_len: int) -> int:
        s = list(accumulate(nums, initial=0))
        n = len(s)

        def f(a: int, b: int) -> int:
            ans = mx = 0
            for i in range(a + b, n):
                mx = max(mx, s[i - a] - s[i - a - b])
                ans = max(ans, s[i] - s[i - a] + mx)
            return ans

        return max(f(first_len, second_len), f(second_len, first_len))


class SolutionB(Solution):
    @override
    def max_sum_two_no_overlap(self, nums: list[int], first_len: int, second_len: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = a = b = 0
        for i in range(first_len + second_len, len(s)):
            a = max(a, s[i - first_len] - s[i - first_len - second_len])
            b = max(b, s[i - second_len] - s[i - first_len - second_len])
            ans = max(ans, s[i] - s[i - first_len] + a, s[i] - s[i - second_len] + b)
        return ans
