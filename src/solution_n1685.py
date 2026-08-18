from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    """
    给你一个非递减有序整数数组 nums
    请你建立并返回一个整数数组 result, 它跟 nums 长度相等,
    且 result[i] 等于 nums[i] 与数组中所有其他元素差的绝对值之和
    换句话说, result[i] 等于 sum(|nums[i] - nums[j]|),
    其中 0 <= j < nums.length 且 j != i (下标从 0 开始).

    2 <= nums.length <= 10^5
    1 <= nums[i] <= nums[i + 1] <= 10^4
    """

    @abstractmethod
    def get_sum_absolute_differences(self, nums: list[int]) -> list[int]:
        pass


class SolutionA(Solution):
    @override
    def get_sum_absolute_differences(self, nums: list[int]) -> list[int]:
        ans = []
        for i, x in enumerate(nums):
            s = 0
            for j, y in enumerate(nums):
                if i != j:
                    s += abs(x - y)
            ans.append(s)
        return ans


class SolutionB(Solution):
    """
    前缀和
    """

    @override
    def get_sum_absolute_differences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))
        ans = []
        for i, x in enumerate(nums):
            a = x * i - pre[i]
            b = (pre[n] - pre[i]) - x * (n - i)
            ans.append(a + b)
        return ans
