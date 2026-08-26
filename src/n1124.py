from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def longest_WPI(self, hours: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和 + 单调栈
    """

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        n = len(hours)
        stk = [0]
        pre = list(accumulate(hours, lambda a, x: a + (1 if x > 8 else -1), initial=0))
        for j in range(1, n + 1):
            if pre[j] < pre[stk[-1]]:
                stk.append(j)
        ans = 0
        for i in range(n, 0, -1):
            while stk and pre[i] > pre[stk[-1]]:
                ans = max(ans, i - stk.pop())
        return ans


class SolutionB(Solution):
    """
    单调栈 + 前缀和
    优化: 将前缀和的计算合并到单点找的遍历中
    """

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        n = len(hours)
        stk = [0]
        pre = [0]
        for j in range(1, n + 1):
            pre.append(pre[-1] + (1 if hours[j - 1] > 8 else -1))
            if pre[j] < pre[stk[-1]]:
                stk.append(j)
        ans = 0
        for i in range(n, 0, -1):
            while stk and pre[i] > pre[stk[-1]]:
                ans = max(ans, i - stk.pop())
        return ans


class SolutionC(Solution):
    """
    前缀和 + hash表
    利用前缀和每次只±1的特性
    """

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        pre = ans = 0
        cnt = {0: -1}
        for i, x in enumerate(hours):
            pre += 1 if x > 8 else -1
            if pre > 0:
                ans = i + 1
            else:
                if pre - 1 in cnt:
                    ans = max(ans, i - cnt[pre - 1])
                if pre not in cnt:
                    cnt[pre] = i
        return ans
