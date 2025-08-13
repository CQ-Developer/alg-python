from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximum_triple_value(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    前后缀
    """

    @override
    def maximum_triple_value(self, nums: list[int]) -> int:
        n = len(nums)
        r_max = [0] * (n + 1)
        for i in range(n - 1, 1, -1):
            r_max[i] = max(r_max[i + 1], nums[i])
        res = 0
        l_max = nums[0]
        for j, x in enumerate(nums[1:], 1):
            res = max(res, (l_max - x) * r_max[j + 1])
            l_max = max(l_max, x)
        return res


class SolutionB(Solution):
    """
    动态规划
    """

    @override
    def maximum_triple_value(self, nums: list[int]) -> int:
        res = dif = pre = 0
        for x in nums:
            res = max(res, dif * x)
            dif = max(dif, pre - x)
            pre = max(pre, x)
        return res
