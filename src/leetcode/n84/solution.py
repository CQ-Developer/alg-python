from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def largest_rectangle_area(self, heights: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def largest_rectangle_area(self, heights: list[int]) -> int:
        n = len(heights)
        stk = []
        left, right = [-1] * n, [n] * n
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk.clear()
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while stk and heights[stk[-1]] >= h:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        mx = 0
        for l, r, h in zip(left, right, heights):
            mx = max(mx, h * (r - l - 1))
        return mx


class SolutionB(Solution):

    @override
    def largest_rectangle_area(self, heights: list[int]) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n
        stk = []
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                right[stk.pop()] = i
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        mx = 0
        for l, r, h in zip(left, right, heights):
            mx = max(mx, h * (r - l - 1))
        return mx


class SolutionC(Solution):

    @override
    def largest_rectangle_area(self, heights: list[int]) -> int:
        heights.append(-1)
        mx = 0
        st = [-1]
        for r, x in enumerate(heights):
            while len(st) > 1 and x <= heights[st[-1]]:
                h = heights[st.pop()]
                mx = max(mx, h * (r - st[-1] - 1))
            st.append(r)
        return mx
