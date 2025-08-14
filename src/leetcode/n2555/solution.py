from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximize_win(self, prize_positions: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximize_win(self, prize_positions: list[int], k: int) -> int:
        n = len(prize_positions)
        if k * 2 + 1 >= prize_positions[-1] - prize_positions[0]:
            return n
        mx = [0] * (n + 1)
        res = l = 0
        for r, p in enumerate(prize_positions):
            while p - prize_positions[l] > k:
                l += 1
            res = max(res, mx[l] + r - l + 1)
            mx[r + 1] = max(mx[r], r - l + 1)
        return res
