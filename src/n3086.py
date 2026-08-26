import abc
import itertools
import math
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def minimum_moves(self, nums: list[int], k: int, max_changes: int) -> int:
        pass


class SolutionA(Solution):
    """
    操作次数的分析:
    1. 当前位置的 1
       操作 0 次
    2. 当前位置左右相邻的 1
       操作 1 次
    3. 第一种操作生成 1
       第二种操作移动 1
       操作 2 次
    4. 第二种操作把 j 的 1 移动到 i
       操作 | i - j | 次

    优先做哪些操作分析:
    1. 先把 i - 1, i, i + 1 这三个位置, 至多 3 个 1 收集到
    2. 用第一种 + 第二种操作得到之多 maxChanges 个 1
    3. 如果还有需要得到的 1, 则用第二种操作, 次数为 | i - j |

    先处理 maxChanges 较大的情况
    """

    @typing.override
    def minimum_moves(self, nums: list[int], k: int, max_changes: int) -> int:
        pos = []
        c = 0
        for i, x in enumerate(nums):
            if x == 0:
                continue
            pos.append(i)
            c = max(c, 1)
            if i > 0 and nums[i - 1] == 1:
                if i > 1 and nums[i - 2] == 1:
                    c = 3
                else:
                    c = max(c, 2)

        c = min(c, k)
        if max_changes >= k - c:
            return max(c - 1, 0) + (k - c) * 2

        n = len(pos)
        pre_sum = list(itertools.accumulate(pos, initial=0))

        ans = math.inf
        size = k - max_changes
        for r in range(size, n + 1):
            l = r - size
            i = (l + r) // 2
            s1 = pos[i] * (i - l) - (pre_sum[i] - pre_sum[l])
            s2 = pre_sum[r] - pre_sum[l] - pos[i] * (r - i)
            ans = min(ans, s1 + s2)

        return int(ans) + max_changes * 2
