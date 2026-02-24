from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_balanced_subarray(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_balanced_subarray(self, nums: list[int]) -> int:
        xor = dif = ans = 0
        cnt = {(0, 0): -1}
        for i, x in enumerate(nums):
            xor ^= x
            dif += (x & 1) * 2 - 1
            k = (xor, dif)
            if k in cnt:
                ans = max(ans, i - cnt[k])
            else:
                cnt[k] = i
        return ans
