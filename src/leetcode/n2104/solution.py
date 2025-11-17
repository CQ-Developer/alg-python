from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def sub_array_ranges(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    '''
    动态规划
    '''

    @override
    def sub_array_ranges(self, nums: list[int]) -> int:
        n = len(nums)
        rng = 0
        for r in range(n):
            mn = mx = nums[r]
            for l in range(r, -1, -1):
                mn, mx = min(mn, nums[l]), max(mx, nums[l])
                rng += mx - mn
        return rng


class SolutionB(Solution):
    '''
    单调栈
    '''

    def sub_array_ranges(self, nums: list[int]) -> int:
        n = len(nums)

        def resolve(nums: list[int]) -> int:
            left, right = [0] * n, [n] * n
            stk = [-1]
            for i, x in enumerate(nums):
                while len(stk) > 1 and nums[stk[-1]] >= x:
                    right[stk.pop()] = i
                left[i] = stk[-1]
                stk.append(i)
            return sum((l - i) * (r - i) * x for i, (x, l, r) in enumerate(zip(nums, left, right)))

        return resolve(nums) + resolve([-x for x in nums])
