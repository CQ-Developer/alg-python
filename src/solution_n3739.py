from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override

from sortedcontainers import SortedList


class Solution(ABC):
    @abstractmethod
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = pre = f = 0
        for x in nums:
            if x == target:
                f += cnt[pre]
                pre += 1
            else:
                pre -= 1
                f -= cnt[pre]
            ans += f
            cnt[pre] += 1
        return ans


class SolutionB(Solution):
    @override
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        s = n = len(nums)
        cnt = [0] * (2 * n + 1)
        cnt[n] = 1
        ans = f = 0
        for x in nums:
            if target == x:
                f += cnt[s]
                s += 1
            else:
                s -= 1
                f -= cnt[s]
            ans += f
            cnt[s] += 1
        return ans


class SolutionC(Solution):
    @override
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        cnt = SortedList([0])
        ans = pre = 0
        for x in nums:
            pre += 1 if x == target else -1
            ans += cnt.bisect_left(pre)
            cnt.add(pre)
        return ans
