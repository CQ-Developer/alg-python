from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_subarrays(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_subarrays(self, nums: list[int], k: int) -> int:
        mx = max(nums)
        l = cnt = ans = 0
        for v in nums:
            if mx == v:
                cnt += 1
            while cnt >= k:
                if nums[l] == mx:
                    cnt -= 1
                l += 1
            ans += l
        return ans
