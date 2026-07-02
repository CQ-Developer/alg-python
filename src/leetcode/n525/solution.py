import abc
import itertools
import typing


class Solution(abc.ABC):
    """
    找到含有相同数量的0和1的最长连续子数组的长度
    """

    @abc.abstractmethod
    def find_max_length(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @typing.override
    def find_max_length(self, nums: list[int]) -> int:
        ans = 0
        tab = {}
        for i, x in enumerate(itertools.accumulate((x * 2 - 1 for x in nums), initial=0)):
            if x in tab:
                ans = max(ans, i - tab[x])
            else:
                tab[x] = i
        return ans


class SolutionB(Solution):
    """
    前缀和
    """

    @typing.override
    def find_max_length(self, nums: list[int]) -> int:
        ans = pre = 0
        table = {0: -1}
        for i, x in enumerate(nums):
            pre += x * 2 - 1
            if pre in table:
                ans = max(ans, i - table[pre])
            else:
                table[pre] = i
        return ans
