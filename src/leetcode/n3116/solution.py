from abc import ABC, abstractmethod
from typing import override
from math import lcm
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        n = len(coins)

        def check(x: int) -> int:
            cnt = 0
            for s in range(1, 1 << n):
                y = 1
                for i, v in enumerate(coins):
                    if 1 << i & s:
                        y = lcm(v, y)
                        if y > x:
                            break
                else:
                    cnt += x // y if s.bit_count() & 1 else -(x // y)
            return cnt

        l, r = k - 1, min(coins) * k
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid) >= k:
                r = mid
            else:
                l = mid
        return r


class SolutionB(Solution):

    @override
    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        coins.sort()
        arr = [coins[0]]
        for x in coins[1:]:
            if all(x % y for y in arr):
                arr.append(x)
        subs = [1] * (1 << len(arr))
        for i, x in enumerate(arr):
            s = 1 << i
            for m in range(s):
                subs[s | m] = lcm(subs[m], x)

        def check(x: int) -> bool:
            cnt = 0
            for s in range(1, len(subs)):
                cnt += x // subs[s] if s.bit_count() & 1 else -(x // subs[s])
            return cnt >= k

        return bisect_left(range(k * arr[0]), True, k, key=check)
