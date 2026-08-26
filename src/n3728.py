from abc import ABC, abstractmethod
from collections import defaultdict
from itertools import pairwise
from typing import override


class Solution(ABC):
    """
    统计符合 a[l] = a[r] = sum( a[l + 1] ... a[r - 1]) 的数量
    """

    @abstractmethod
    def count_stable_subarrays(self, capacity: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    推导
    - r - l + 1 >= 3
    - cap[r] = cap[l]
    - pre[r] = cap[l] + pre[l + 1]

    结论
    - r - l > 1
    - (cap[r], pre[r]) = (cap[l], cap[l] + pre[l + 1])

    补充
    通过先计算 r，再更新 r - 1,
    对于下一轮 r + 1 来说, (r + 1)-(r - 1) = 2 > 1
    天然满足了长度要求
    """

    @override
    def count_stable_subarrays(self, capacity: list[int]) -> int:
        ans = 0
        pre = capacity[0]
        cnt = defaultdict(int)
        for p, x in pairwise(capacity):
            ans += cnt[(x, pre)]
            cnt[(p, p + pre)] += 1
            pre += x
        return ans
