from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    """
    最长子数组长度
    """

    @abstractmethod
    def max_balanced_subarray(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @override
    def max_balanced_subarray(self, nums: list[int]) -> int:
        ans = xor = pre = 0
        cnt = {(0, 0): -1}
        for i, x in enumerate(nums):
            xor ^= x
            pre += (x & 1) * 2 - 1
            key = (xor, pre)
            if key in cnt:
                ans = max(ans, i - cnt[key])
            else:
                cnt[key] = i
        return ans
