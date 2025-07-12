from abc import ABC, abstractmethod


class TreeNode:

    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(ABC):

    @abstractmethod
    def count_nodes(self, root: TreeNode | None) -> int:
        pass
