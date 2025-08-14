from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_quadruplets(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_quadruplets(self, nums: list[int]) -> int:
        cnt, n = 0, len(nums)
        for d in range(3, n):
            for c in range(2, d):
                for b in range(1, c):
                    for a in range(0, b):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            cnt += 1
        return cnt


class SolutionB(Solution):

    @override
    def count_quadruplets(self, nums: list[int]) -> int:
        n, cnt = len(nums), 0
        tab = [0] * 301
        for c in range(n - 2, 1, -1):
            tab[nums[c + 1]] += 1
            for b in range(c - 1, 0, -1):
                for a in range(b - 1, -1, -1):
                    cnt += tab[nums[a] + nums[b] + nums[c]]
        return cnt


class SolutionC(Solution):

    @override
    def count_quadruplets(self, nums: list[int]) -> int:
        cnt = 0
        tab = [0] * 301
        for i in range(len(nums) - 3, 0, -1):
            c = nums[i + 1]
            for d in nums[i + 2 :]:
                tab[d - c + 100] += 1
            b = nums[i]
            for a in nums[:i]:
                cnt += tab[a + b + 100]
        return cnt
