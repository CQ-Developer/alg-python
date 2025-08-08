from abc import ABC, abstractmethod
from collections import defaultdict, Counter
from typing import override


class Solution(ABC):

    @abstractmethod
    def pair_sums(self, nums: list[int], target: int) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def pair_sums(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        tab = defaultdict(int)
        for num in nums:
            x = target - num
            if tab[x]:
                res.append([x, num])
                tab[x] -= 1
            else:
                tab[num] += 1
        return res


class SolutionB(Solution):

    @override
    def pair_sums(self, nums: list[int], target: int) -> list[list[int]]:
        cnt = Counter(nums)
        res = []
        for num in cnt:
            x = target - num
            if num > x:
                continue
            if num == x:
                res += [[x, x]] * (cnt[x] // 2)
            elif x in cnt:
                res += [[num, x]] * min(cnt[x], cnt[num])
        return res
