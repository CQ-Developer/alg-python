from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_quadruplets(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_quadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        great = [None] * n
        great[-1] = [0] * (n + 1)
        for k in range(n - 2, 1, -1):
            great[k] = great[k + 1][:]
            for x in range(1, nums[k + 1]):
                great[k][x] += 1
        ans = 0
        less = [0] * (n + 1)
        for j in range(1, n - 2):
            for x in range(nums[j - 1] + 1, n + 1):
                less[x] += 1
            for k in range(j + 1, n - 1):
                if nums[k] < nums[j]:
                    ans += less[nums[k]] * great[k][nums[j]]
        return ans


class SolutionB(Solution):

    @override
    def count_quadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        great = [None] * n
        great[-1] = [0] * (n + 1)
        for k in range(n - 2, 1, -1):
            great[k] = great[k + 1][:]
            for x in range(1, nums[k + 1]):
                great[k][x] += 1
        ans = 0
        for j in range(1, n - 2):
            for k in range(j + 1, n - 1):
                if nums[k] < nums[j]:
                    ans += (nums[k] - n + 1 + j + great[j][nums[k]]) * great[k][nums[j]]
        return ans
