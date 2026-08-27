import abc
import bisect
import itertools
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def answer_queries(self, nums: list[int], queries: list[int]) -> list[int]:
        pass


class SolutionA(Solution):
    """
    前缀和 + 二分
    """

    @typing.override
    def answer_queries(self, nums: list[int], queries: list[int]) -> list[int]:
        p = list(itertools.accumulate(sorted(nums)))
        return [bisect.bisect_right(p, q) for q in queries]


class SolutionB(Solution):
    """
    空间优化
    """

    @typing.override
    def answer_queries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        for i, q in enumerate(queries):
            queries[i] = bisect.bisect_right(nums, q)
        return queries
