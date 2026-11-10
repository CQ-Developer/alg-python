from __future__ import annotations

from collections import deque
from typing import Any


def build_tree(node_cls: type[Any], values: list[Any | None]) -> Any | None:
    """Build a tree from a LeetCode level-order array."""
    if not values or values[0] is None:
        return None

    root = node_cls(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()

        if index < len(values):
            value = values[index]
            index += 1
            if value is not None:
                node.left = node_cls(value)
                queue.append(node.left)

        if index < len(values):
            value = values[index]
            index += 1
            if value is not None:
                node.right = node_cls(value)
                queue.append(node.right)

    return root


def tree_to_list(root: Any | None) -> list[Any | None]:
    """Serialize a tree to a LeetCode level-order array, trimming trailing nulls."""
    if root is None:
        return []

    result: list[Any | None] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()
    return result


def build_list(node_cls: type[Any], values: list[Any]) -> Any | None:
    """Build a singly linked list from an array."""
    dummy = node_cls(0)
    current = dummy
    for value in values:
        current.next = node_cls(value)
        current = current.next
    return dummy.next
