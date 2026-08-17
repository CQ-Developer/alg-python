from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution(ABC):
    """
    给定一个二叉树的根节点 root, 和一个整数 target_sum,
    求该二叉树里节点值之和等于 target_sum 的路径的数目.
    路径不需要从根节点开始, 也不需要在叶子节点结束,
    但是路径方向必须是向下的 (只能从父节点到子节点)

    二叉树的节点个数的范围是 [0, 1000]
    -10^9 <= Node.val <= 10^9
    -1000 <= target_sum <= 1000
    """

    @abstractmethod
    def path_sum(self, root: TreeNode | None, target_sum: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和 + 回溯
    """

    @override
    def path_sum(self, root: TreeNode | None, target_sum: int) -> int:
        cnt = defaultdict(int)
        cnt[0] += 1

        def _dfs(node: TreeNode | None, pre: int) -> int:
            if node is None:
                return 0
            pre += node.val
            ans = cnt[pre - target_sum]
            cnt[pre] += 1
            ans += _dfs(node.left, pre)
            ans += _dfs(node.right, pre)
            cnt[pre] -= 1
            return ans

        return _dfs(root, 0)
