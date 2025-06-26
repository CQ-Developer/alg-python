import heapq
from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def k_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def k_sum(self, nums: list[int], k: int) -> int:
        s = 0
        for i, x in enumerate(nums):
            if x >= 0:
                s += x
            else:
                nums[i] = -x
        nums.sort()
        x, n = 0, len(nums)
        h = [(nums[0], 0)]
        for _ in range(1, k):
            x, i = heapq.heappop(h)
            if i + 1 < n:
                heapq.heappush(h, (x + nums[i + 1], i + 1))
                heapq.heappush(h, (x - nums[i] + nums[i + 1], i + 1))
        return s - x


class SolutionB(Solution):

    @override
    def k_sum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def check(x: int) -> bool:
            cnt = 1

            def dfs(i: int, s: int):
                nonlocal cnt
                if i == n or s + nums[i] > x or cnt == k:
                    return
                cnt += 1
                dfs(i + 1, s)
                dfs(i + 1, s + nums[i])

            dfs(0, 0)
            return cnt == k

        s = 0
        for i, x in enumerate(nums):
            if x >= 0:
                s += x
            else:
                nums[i] = -x
        nums.sort()
        return s - bisect_left(range(sum(nums)), True, key=check)
