from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def check(x: int) -> int:
            j, cnt = 1, 0
            for i, v in enumerate(nums):
                while j < n and nums[j] - v <= x:
                    j += 1
                cnt += j - i - 1
            return cnt

        l, r = 0, nums[-1] - nums[0] + 1
        while l < r:
            mid = (l + r) // 2
            if check(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return r


class SolutionB(Solution):

    @override
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        def check(x: int) -> int:
            l = cnt = 0
            for r, v in enumerate(nums):
                while v - nums[l] > x:
                    l += 1
                cnt += r - l
            return cnt

        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            mid = (l + r) // 2
            if check(mid) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l
