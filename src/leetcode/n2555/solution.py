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


class SolutionB(Solution):

    def maximize_win(self, prize_positions: list[int], k: int) -> int:
        n = len(prize_positions)
        if k * 2 + 1 >= prize_positions[-1] - prize_positions[0]:
            return n
        res = mx = l = r = 0
        for i, p in enumerate(prize_positions):
            while r < n and prize_positions[r] - p <= k:
                r += 1
            res = max(res, mx + r - i)
            while p - prize_positions[l] > k:
                l += 1
            mx = max(mx, i - l + 1)
        return res
