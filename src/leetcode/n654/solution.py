from abc import ABC, abstractmethod
from typing import override


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, TreeNode):
            return False
        if self.val != other.val:
            return False
        if (self.left is None) != (other.left is None):
            return False
        if self.left is not None and self.left != other.left:
            return False
        if (self.right is None) != (other.right is None):
            return False
        if self.right is not None and self.right != other.right:
            return False
        return True


class Solution(ABC):

    @abstractmethod
    def construct_maximum_binary_tree(self, nums: list[int]) -> TreeNode | None:
        pass


class SolutionA(Solution):

    @override
    def construct_maximum_binary_tree(self, nums: list[int]) -> TreeNode | None:
        if nums:
            v, i = max((v, i) for i, v in enumerate(nums))
            return TreeNode(v, self.construct_maximum_binary_tree(nums[:i]), self.construct_maximum_binary_tree(nums[i + 1 :]))


class SolutionB(Solution):

    @override
    def construct_maximum_binary_tree(self, nums: list[int]) -> TreeNode | None:
        stk = []
        nodes = [TreeNode() for _ in nums]
        for i, x in enumerate(nums):
            nodes[i].val = x
            while stk and x > nums[stk[-1]]:
                nodes[i].left = nodes[stk.pop()]
            if stk:
                nodes[stk[-1]].right = nodes[i]
            stk.append(i)
        return nodes[stk[0]]
