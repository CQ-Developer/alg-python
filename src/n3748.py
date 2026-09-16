from abc import ABC, abstractmethod
from bisect import bisect_right
from typing import override


class Solution(ABC):
    @abstractmethod
    def count_stable_subarrays(
        self,
        nums: list[int],
        queries: list[list[int]],
    ) -> list[int]:
        pass


class SolutionA(Solution):
    """
    前缀和 + 二分查找
    """

    @override
    def count_stable_subarrays(
        self,
        nums: list[int],
        queries: list[list[int]],
    ) -> list[int]:
        n = len(nums)
        left = []
        pre = [0]
        start = 0
        for i, x in enumerate(nums):
            if i == n - 1 or x > nums[i + 1]:
                left.append(start)
                m = i + 1 - start
                pre.append(pre[-1] + m * (m + 1) // 2)
                start = i + 1
        ans = []
        for l, r in queries:
            i = bisect_right(left, l)
            j = bisect_right(left, r) - 1
            if j < i:
                m = r + 1 - l
                ans.append(m * (m + 1) // 2)
            else:
                m1 = left[i] - l
                m2 = r + 1 - left[j]
                ans.append(m1 * (m1 + 1) // 2 + (pre[j] - pre[i]) + m2 * (m2 + 1) // 2)
        return ans


class SolutionB(Solution):
    @override
    def count_stable_subarrays(
        self,
        nums: list[int],
        queries: list[list[int]],
    ) -> list[int]:
        n = len(nums)
        # 计算递增子数组数量的前缀和
        cnt = 0
        s = [0] * (n + 1)
        for i, x in enumerate(nums):
            if x > 0 and x < nums[i - 1]:
                cnt = 0
            cnt += 1
            s[i + 1] = s[i] + cnt
        # nxt[i] 表示 i 右侧下一个递增子数组的左端点
        # 若不存在则为 n
        nxt = [0] * n
        nxt[-1] = n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nxt[i] = nxt[i + 1]
            else:
                nxt[i] = i + 1
        ans = []
        for l, r in queries:
            l2 = nxt[l]
            if l2 > r:
                # l, r 在同一段
                m = r + 1 - l
                ans.append(m * (m + 1) // 2)
            else:
                # 分别计算 [l, l2) 和 [l2, r]
                m = l2 - l
                ans.append(m * (m + 1) // 2 + s[r + 1] - s[l2])
        return ans
