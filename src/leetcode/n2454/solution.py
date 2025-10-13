import heapq
from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def second_greater_element(self, nums: list[int]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def second_greater_element(self, nums: list[int]) -> list[int]:
        s, h = [], []
        a = [-1] * len(nums)
        for i, x in enumerate(nums):
            while h and x > h[0][0]:
                a[heapq.heappop(h)[1]] = x
            while s and x > nums[s[-1]]:
                j = s.pop()
                heapq.heappush(h, [nums[j], j])
            s.append(i)
        return a


class SolutionB(Solution):

    @override
    def second_greater_element(self, nums: list[int]) -> list[int]:
        a = [-1] * len(nums)
        s1, s2 = [], []
        for i, x in enumerate(nums):
            while s2 and x > nums[s2[-1]]:
                a[s2.pop()] = x
            t = []
            while s1 and x > nums[s1[-1]]:
                t.append(s1.pop())
            while t:
                s2.append(t.pop())
            s1.append(i)
        return a
