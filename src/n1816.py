from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    """
    给你一个整数数组 nums，
    请你返回所有下标对 0 <= i, j < nums.length 的 floor(nums[i] / nums[j]) 结果之和。
    由于答案可能会很大，请你返回答案对 10^9 + 7 取余的结果。
    """

    @abstractmethod
    def sum_of_floored_pairs(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    @override
    def sum_of_floored_pairs(self, nums: list[int]) -> int:
        return 0
