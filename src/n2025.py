from abc import ABC, abstractmethod
from collections import Counter
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def ways_to_partition(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    """
    假设数组和为 total, 前缀和数组为 pre
    存在切割点 i, 使得 pre[i] = total - pre[i]

    关键论证:
    将 nums[i] 改成 k, 则 d = k - nums[i]
    这时总和变成 total + d

    1. 假设需要修改的 nums[i] 在切割点 p 的右侧, 即 p <= i
    这时左侧不变, 右侧发生变化
    pre[i] = total + d - pre[i] 移项后得到: pre[i] = (total + d) / 2

    2. 假设需要修改的 nums[i] 在切割点 p 的左侧, 即 p > i
    这是左侧发生变化, 右侧不变
    pre[i] + d = total - pre[i] 移项后得到: pre[i] = (total - d) / 2

    加入存在这个样的 nums[i] 在变化后能使得数平衡,
    那么 x 个 nums[i] 就能为答案贡献 x, 所以需要使用 2
    个表, 分别统计这样的 nums[i] 在切割点的左右分别有
    多少个.
    """

    @override
    def ways_to_partition(self, nums: list[int], k: int) -> int:
        pre = list(accumulate(nums, initial=0))
        total = pre[-1]
        cnt_l, cnt_r = Counter(), Counter(pre[1:-1])
        # 不分割
        ans = cnt_r[total // 2] if total % 2 == 0 else 0
        # 枚举修改点
        for i, x in enumerate(nums):
            d = k - x
            if (total + d) % 2 == 0:
                ans = max(ans, cnt_l[(total + d) // 2] + cnt_r[(total - d) // 2])
            cnt_l[pre[i + 1]] += 1
            cnt_r[pre[i + 1]] -= 1
        return ans
