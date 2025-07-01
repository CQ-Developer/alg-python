from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class TreeNode:

    def __init__(self, val: int = 0, left: 'TreeNode|None' = None, right: 'TreeNode|None' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(ABC):

    @abstractmethod
    def closest_nodes(self, root: TreeNode | None, queries: list[int]) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def closest_nodes(self, root: TreeNode | None, queries: list[int]) -> list[list[int]]:
        a: list[int] = []
        res: list[list[int]] = []

        def dfs(root: TreeNode | None):
            if root is None:
                return
            dfs(root.left)
            a.append(root.val)
            dfs(root.right)

        dfs(root)
        n = len(a)

        for x in queries:
            i = bisect_left(a, x)
            mx = a[i] if i < n else -1
            if i == n or a[i] != x:
                i -= 1
            mn = a[i] if i >= 0 else -1
            res.append([mn, mx])
        return res
