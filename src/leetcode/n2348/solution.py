from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def zero_filled_subarray(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    '''
    动态规划
    '''

    @override
    def zero_filled_subarray(self, nums: list[int]) -> int:
        f = [0] * len(nums)
        for i, x in enumerate(nums):
            if x == 0:
                f[i] = 1
                if i > 0 and nums[i - 1] == 0:
                    f[i] += f[i - 1]
        return sum(f)


class SolutionB(Solution):
    '''
    空间压缩动态规划
    '''

    @override
    def zero_filled_subarray(self, nums: list[int]) -> int:
        a = p = 0
        for i, x in enumerate(nums):
            if x == 0:
                c = 1
                if i > 0 and nums[i - 1] == 0:
                    c += p
                a += c
                p = c
        return a


class SolutionC(Solution):
    '''
    滑动窗口: p表示上一个非0数字的下标
    '''

    @override
    def zero_filled_subarray(self, nums: list[int]) -> int:
        a, p = 0, -1
        for i, x in enumerate(nums):
            if x:
                p = i
            else:
                a += i - p
        return a


class SolutionD(Solution):
    '''
    贡献法: p表示之前的连续0的个数
    '''

    @override
    def zero_filled_subarray(self, nums: list[int]) -> int:
        p = a = 0
        for x in nums:
            if x:
                p = 0
            else:
                p += 1
                a += p
        return a


class SolutionE(Solution):
    '''
    双指针
    '''

    @override
    def zero_filled_subarray(self, nums: list[int]) -> int:
        i = a = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                j = i
                while i + 1 < n and nums[i + 1] == 0:
                    i += 1
                m = i - j + 1
                a += m * (m + 1) // 2
            i += 1
        return a
