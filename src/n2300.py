from abc import ABC, abstractmethod
from bisect import bisect_right
from typing import override


class Solution(ABC):
    @abstractmethod
    def successful_pairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pass


class SolutionA(Solution):
    """
    暴力解
    """

    @override
    def successful_pairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pairs = []
        for x in spells:
            cnt = 0
            for y in potions:
                if x * y >= success:
                    cnt += 1
            pairs.append(cnt)
        return pairs


class SolutionB(Solution):
    """
    二分查找
    """

    @override
    def successful_pairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        success -= 1
        return [m - bisect_right(potions, success // x) for x in spells]


class SolutionC(Solution):
    """
    后缀和
    """

    @override
    def successful_pairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        # 统计每种 potion 出现的次数
        mx = max(potions)
        cnt = [0] * (mx + 1)
        for x in potions:
            cnt[x] += 1
        # 计算 cnt 的后缀和
        for i in range(mx - 1, -1, -1):
            cnt[i] += cnt[i + 1]
        # 枚举每个 spell 需要的最少 potion 数量
        for i, x in enumerate(spells):
            low = (success - 1) // x + 1
            spells[i] = cnt[low] if low <= mx else 0
        return spells
