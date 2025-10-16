from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def maximum_sum_queries(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def maximum_sum_queries(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        max_sums = [-1] * len(queries)
        j = 0
        pairs = sorted(((a, b) for a, b in zip(nums1, nums2)), key=lambda p: -p[0])
        stack: list[tuple[int, int]] = []
        for i, (x, y) in sorted(enumerate(queries), key=lambda q: -q[1][0]):
            while j < len(pairs) and pairs[j][0] >= x:
                a, b = pairs[j]
                while stack and stack[-1][1] <= a + b:
                    stack.pop()
                if not stack or stack[-1][0] < b:
                    stack.append((b, a + b))
                j += 1
            p = bisect_left(stack, (y,))
            if p < len(stack):
                max_sums[i] = stack[p][1]
        return max_sums
