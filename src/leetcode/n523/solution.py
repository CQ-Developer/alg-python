from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        pass


class SolutionA(Solution):

    @override
    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        p = 0
        cnt = {0: -1}
        for i, x in enumerate(nums):
            p = (p + x) % k
            if p in cnt:
                if i - cnt[p] >= 2:
                    return True
            else:
                cnt[p] = i
        return False
