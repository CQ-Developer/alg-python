from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def see_people(self, heights: list[list[int]]) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def see_people(self, heights: list[list[int]]) -> list[list[int]]:
        def f(nums: list[int] | tuple[int, ...]) -> list[int]:
            ans, stk = [0] * len(nums), []
            for i, x in reversed(list(enumerate(nums))):
                while stk and x > stk[-1]:
                    ans[i] += 1
                    stk.pop()
                if stk:
                    ans[i] += 1
                while stk and x == stk[-1]:
                    stk.pop()
                stk.append(x)
            return ans

        n = len(heights)
        ans = [f(nums) for nums in heights]
        for j, cnt in enumerate(map(f, zip(*heights))):
            for i in range(n):
                ans[i][j] += cnt[i]
        return ans
