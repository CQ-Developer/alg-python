from abc import ABC, abstractmethod
from collections import defaultdict, Counter
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_operations(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_operations(self, nums: list[int], k: int) -> int:
        res = 0
        tab = defaultdict(int)
        for num in nums:
            if tab[k - num] > 0:
                res += 1
                tab[k - num] -= 1
            else:
                tab[num] += 1
        return res


class SolutionB(Solution):

    @override
    def max_operations(self, nums: list[int], k: int) -> int:
        res = 0
        cnt = Counter(nums)
        for num in cnt:
            x = k - num
            if num > x:
                continue
            if num == x:
                res += cnt[x] // 2
            elif x in cnt:
                res += min(cnt[num], cnt[x])
        return res
