from abc import ABC, abstractmethod
from typing import override


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

        def in_order_traversal(root: TreeNode | None):
            if root is None:
                return
            in_order_traversal(root.left)
            a.append(root.val)
            in_order_traversal(root.right)

        in_order_traversal(root)
        n = len(a)

        for x in queries:
            l, r = -1, n
            while l + 1 < r:
                i = (l + r) // 2
                if a[i] >= x:
                    r = i
                else:
                    l = i
            mx = a[r] if r < n else -1
            if r == n or a[r] != x:
                r -= 1
            mn = a[r] if r >= 0 else -1
            res.append([mn, mx])
        return res
