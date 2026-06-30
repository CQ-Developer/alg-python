from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):
    """
    统计美丽子数组数目
    """

    @abstractmethod
    def beautiful_subarrays(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和:
    1. `pre[i + 1] = nums[0] ^ nums[1] ^ ... ^ nums[i]`
    2. `nums[l...r] = pre[r + 1] ^ pre[l]`

    求:
    - nums[l...r] = 0

    推导:
    - `pre[r + 1] ^ pre[l] = 0`
    - `pre[r + 1] = pre[l]`
    """

    @override
    def beautiful_subarrays(self, nums: list[int]) -> int:
        ans = pre = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[pre] += 1
            pre ^= x
            ans += cnt[pre]
        return ans
