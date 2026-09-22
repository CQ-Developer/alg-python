from abc import ABC, abstractmethod
from math import inf
from typing import override


class Solution(ABC):
    @abstractmethod
    def max_difference(self, s: str, k: int) -> int:
        pass


class SolutionA(Solution):
    """
    定义 sum[i + 1][j] 表示 s[0] 中的 j 的出现次.
    枚举数字 x 和 y,
    对于子串 [l, r), 有 sum[r][x] - sum[l][x] 个 x, 以及 sum[r][y] - sum[l][y] 个 y

    求如下结果的最大值
    (sum[r][x] - sum[l][x]) - (sum[r][y] - sum[l][y]) = (sum[r][x] - sum[r][y]) - (sum[l][x] - sum[l][y])

    满足条件
    - r - l >= k
    - sum[r][x] > sum[l][x]
    - sum[r][y] > sum[l][y]

    min_s[p][q] 表示 min(sum[l][x] - sum[l][y]), 其中
    - sum[l][x] 的奇偶性为 p. 其中 p = 0 表示偶, p = 1 表示奇
    - sum[l][y] 的奇偶性为 q. 其中 q = 0 表示偶, q = 1 表示奇
    """

    @override
    def max_difference(self, s: str, k: int) -> int:
        nums = [int(c) for c in s]
        ans = -inf
        for x in range(5):
            for y in range(5):
                if x == y:
                    continue
                cur_s = [0] * 5
                pre_s = [0] * 5
                min_s = [[inf, inf], [inf, inf]]
                l = 0
                for i, v in enumerate(nums):
                    cur_s[v] += 1
                    r = i + 1
                    while r - l >= k and cur_s[x] > pre_s[x] and cur_s[y] > pre_s[y]:
                        p, q = pre_s[x] & 1, pre_s[y] & 1
                        min_s[p][q] = min(min_s[p][q], pre_s[x] - pre_s[y])
                        pre_s[nums[l]] += 1
                        l += 1
                    if r >= k:
                        ans = max(ans, cur_s[x] - cur_s[y] - min_s[cur_s[x] & 1 ^ 1][cur_s[y] & 1])
        return ans
