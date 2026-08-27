import abc
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def min_cost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @typing.override
    def min_cost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        sr = [0] * n
        sl = [0] * n
        for i in range(1, n):
            # i - 1 -> i
            if i > 1 and nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]:
                sr[i] = sr[i - 1] + nums[i] - nums[i - 1]
            else:
                sr[i] = sr[i - 1] + 1
            # i - 1 <- i
            if i + 1 < n and nums[i] - nums[i - 1] > nums[i + 1] - nums[i]:
                sl[i] = sl[i - 1] + nums[i] - nums[i - 1]
            else:
                sl[i] = sl[i - 1] + 1
        ans = []
        for l, r in queries:
            if l < r:
                ans.append(sr[r] - sr[l])
            else:
                ans.append(sl[l] - sl[r])
        return ans
