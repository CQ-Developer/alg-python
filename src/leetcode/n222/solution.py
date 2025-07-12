from abc import ABC, abstractmethod
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
