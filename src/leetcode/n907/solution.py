from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def sum_subarray_mins(self, arr: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def sum_subarray_mins(self, arr: list[int]) -> int:
        n = len(arr)
        stk = [-1]
        left = [0] * n
        for i, x in enumerate(arr):
            while len(stk) > 1 and arr[stk[-1]] >= x:
                stk.pop()
            left[i] = stk[-1]
            stk.append(i)
        stk = [n]
        right = [n] * n
        for i in range(n - 1, -1, -1):
            while len(stk) > 1 and arr[stk[-1]] > arr[i]:
                stk.pop()
            right[i] = stk[-1]
            stk.append(i)
        s = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            s += x * (i - l) * (r - i)
        return s % (10**9 + 7)


class SolutionB(Solution):

    @override
    def sum_subarray_mins(self, arr: list[int]) -> int:
        n = len(arr)
        left, right = [0] * n, [n] * n
        stk = [-1]
        for i, x in enumerate(arr):
            while len(stk) > 1 and arr[stk[-1]] >= x:
                right[stk.pop()] = i
            left[i] = stk[-1]
            stk.append(i)
        s = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            s += x * (i - l) * (r - i)
        return s % (10**9 + 7)


class SolutionC(Solution):

    @override
    def sum_subarray_mins(self, arr: list[int]) -> int:
        arr.append(-1)
        a = 0
        stk = [-1]
        for r, x in enumerate(arr):
            while len(stk) > 1 and arr[stk[-1]] >= x:
                i = stk.pop()
                a += arr[i] * (i - stk[-1]) * (r - i)
            stk.append(r)
        return a % (10**9 + 7)
