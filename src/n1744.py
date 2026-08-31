import abc
import itertools
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def can_eat(self, candies_count: list[int], queries: list[list[int]]) -> list[bool]:
        pass


class SolutionA(Solution):
    """
    能吃多少糖?
    每天最少吃 1 颗糖, 最多吃 q[2] 颗糖
    那么第 q[1] 天能吃的糖的数量范围 [q[1] + 1, ( q[1] + 1 ) * q[2]]

    糖的数量?
    设 candies_count 的前缀和数组为 s
    第 i 类糖的数量范围 [s[i - 1] + 1, s[i]]

    只要这 2 个区间存在交集就能吃到喜欢的糖
    """

    @typing.override
    def can_eat(self, candies_count: list[int], queries: list[list[int]]) -> list[bool]:
        s = list(itertools.accumulate(candies_count))
        ans = []
        for i, day, cap in queries:
            x1 = day + 1
            y1 = x1 * cap
            x2 = 1 if i == 0 else s[i - 1] + 1
            y2 = s[i]
            ans.append(y1 >= x2 and y2 >= x1)
        return ans
