from abc import ABC, abstractmethod
from collections import deque
from typing import override


class TreeNode:

    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(ABC):

    @abstractmethod
    def count_nodes(self, root: TreeNode | None) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_nodes(self, root: TreeNode | None) -> int:
        if root:
            return self.count_nodes(root.left) + self.count_nodes(root.right) + 1
        return 0


class SolutionB(Solution):

    @override
    def count_nodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q: deque[TreeNode] = deque()
        q.append(root)
        cnt = 0
        while q:
            c = q.popleft()
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)
            cnt += 1
        return cnt


class SolutionC(Solution):

    @override
    def count_nodes(self, root: TreeNode | None) -> int:
        l, cur = 0, root
        while cur:
            l += 1
            cur = cur.left
        r, cur = 0, root
        while cur:
            r += 1
            cur = cur.right
        if l == r:
            return 2 ** l - 1
        return self.count_nodes(root.left) + self.count_nodes(root.right) + 1
