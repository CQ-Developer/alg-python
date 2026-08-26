from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    """
    连续的子数组和
    """

    @abstractmethod
    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        pass


class SolutionA(Solution):
    """
    前缀和 + hash
    """

    @override
    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        pre = 0
        cnt = {0: -1}
        for i, x in enumerate(nums):
            pre = (pre + x) % k
            if pre in cnt:
                if i - cnt[pre] >= 2:
                    return True
            else:
                cnt[pre] = i
        return False
