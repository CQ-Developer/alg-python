from abc import ABC, abstractmethod
from typing import override


M = 10**9 + 7
N = 10**5 + 1

omega = [0] * N
for i in range(2, N):
    if omega[i] == 0:
        for j in range(i, N, i):
            omega[j] += 1


class Solution(ABC):

    @abstractmethod
    def maximum_score(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_score(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left, right = [-1] * n, [n] * n
        stk = []
        for i, x in enumerate(nums):
            while stk and omega[nums[stk[-1]]] < omega[x]:
                right[stk.pop()] = i
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        mx = 1
        for i, v, l, r in sorted(zip(range(n), nums, left, right), key=lambda z: -z[1]):
            s = (i - l) * (r - i)
            if s >= k:
                mx = mx * pow(v, k, M) % M
                break
            mx = mx * pow(v, s, M) % M
            k -= s
        return mx
