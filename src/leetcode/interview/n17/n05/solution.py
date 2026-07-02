import abc
import typing


class Solution(abc.ABC):
    """
    找到最长的子数组，且包含的字母和数字的个数相同。
    返回左端点下标值最小的子数组。
    """

    @abc.abstractmethod
    def find_longest_subarray(self, array: list[str]) -> list[str]:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @typing.override
    def find_longest_subarray(self, array: list[str]) -> list[str]:
        p = n = 0
        pre = 0
        table = {0: -1}
        for i, x in enumerate(array):
            pre += 1 if x.isdigit() else -1
            if pre in table:
                j = table[pre]
                m = i - j
                if m > n:
                    p, n = j, m
            else:
                table[pre] = i
        return array[p + 1 : p + 1 + n]
