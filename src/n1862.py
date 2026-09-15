from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    """
    给你一个整数数组 nums，
    请你返回所有下标对 0 <= i, j < nums.length 的 floor(nums[i] / nums[j]) 结果之和。
    由于答案可能会很大，请你返回答案对 10^9 + 7 取余的结果。
    """

    @abstractmethod
    def sum_of_floored_pairs(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    @override
    def sum_of_floored_pairs(self, nums: list[int]) -> int:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
        s = list(accumulate(cnt, initial=0))
        ans = 0
        # 分母
        for i in range(1, mx + 1):
            cnt_i = cnt[i]
            if cnt_i:
                # 分子
                for j in range(0, mx + 1, i):
                    cnt_j = s[min(mx + 1, j + i)] - s[j]
                    ans = (ans + (j // i) * cnt_i * cnt_j) % 1_000_000_007
        return ans
