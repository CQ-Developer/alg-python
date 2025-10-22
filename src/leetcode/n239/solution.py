from abc import ABC, abstractmethod
from typing import override
from collections import deque


class Solution(ABC):

    @abstractmethod
    def max_sliding_window(self, nums: list[int], k: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def max_sliding_window(self, nums: list[int], k: int) -> list[int]:
        dq, ans = deque(), []
        for i, x in enumerate(nums):
            while dq and x > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if dq[0] < i - k + 1:
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
