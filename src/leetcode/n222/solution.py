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
            return (1 << l) - 1
        return self.count_nodes(root.left) + self.count_nodes(root.right) + 1


class SolutionD(Solution):

    @override
    def count_nodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        h, node = 0, root
        while node.left:
            h += 1
            node = node.left

        def check(k: int) -> TreeNode | None:
            b, node = 1 << (h - 1), root
            while node and b > 0:
                if (b & k) == 0:
                    node = node.left
                else:
                    node = node.right
                b >>= 1
            return node

        l, r = (1 << h), 1 << (h + 1)
        while l + 1 < r:
            i = (l + r) // 2
            if check(i):
                l = i
            else:
                r = i
        return l
