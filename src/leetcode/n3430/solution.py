from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def min_max_subarray_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    """
    单调栈 + 贡献法
    """

    @override
    def min_max_subarray_sum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def contribute(nums: list[int]) -> int:
            st = []
            left, right = [-1] * n, [n] * n
            for i, v in enumerate(nums):
                while st and nums[st[-1]] >= v:
                    right[st.pop()] = i
                if st:
                    left[i] = st[-1]
                st.append(i)
            ans = 0
            for i, (v, l, r) in enumerate(zip(nums, left, right)):
                if r - l - 1 <= k:
                    ans += v * (i - l) * (r - i)
                else:
                    l, r = max(l, i - k), min(r, i + k)
                    a = (r - i) * (i - (r - k))
                    b = (l + r + k + 1 - i * 2) * (r - l - k) // 2
                    ans += v * (a + b)
            return ans

        return contribute(nums) - contribute([-v for v in nums])


class SolutionB(Solution):
    """
    同上: 合并循环
    """

    @override
    def min_max_subarray_sum(self, nums: list[int], k: int) -> int:
        def contribute(nums: list[int]) -> int:
            ans = 0
            st = [-1]
            for r, v in enumerate(nums + [-inf]):
                while len(st) > 1 and nums[st[-1]] >= v:
                    i = st.pop()
                    l = st[-1]
                    if r - l - 1 <= k:
                        ans += nums[i] * (i - l) * (r - i)
                    else:
                        _l, _r = max(l, i - k), min(r, i + k)
                        a = (_r - i) * (i - (_r - k))
                        b = (_l + _r + k + 1 - i * 2) * (_r - _l - k) // 2
                        ans += nums[i] * (a + b)
                st.append(r)
            return ans

        return contribute(nums) - contribute([-v for v in nums])


class SolutionC(Solution):
    """
    同上: 不同的计算方式
    count(l...r) - count(l...i) - count(i...r)
    """

    @override
    def min_max_subarray_sum(self, nums: list[int], k: int) -> int:
        count = lambda n: (2 * n - k + 1) * k // 2 if n > k else (n + 1) * n // 2

        def contribute(nums: list[int]) -> int:
            ans = 0
            st = [-1]
            for r, v in enumerate(nums + [-inf]):
                while len(st) > 1 and nums[st[-1]] >= v:
                    i = st.pop()
                    l = st[-1]
                    ans += nums[i] * (count(r - l - 1) - count(i - l - 1) - count(r - i - 1))
                st.append(r)
            return ans

        return contribute(nums) - contribute([-v for v in nums])
