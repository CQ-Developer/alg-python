from abc import ABC, abstractmethod
from typing import override


class ListNode:

    def __init__(self, val=0, next: 'ListNode|None' = None):
        self.val = val
        self.next = next


class Solution(ABC):

    @abstractmethod
    def next_larger_nodes(self, head: ListNode | None) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def next_larger_nodes(self, head: ListNode | None) -> list[int]:
        i = n = 0
        h = head
        while h:
            n += 1
            h = h.next
        s, r = [], [0] * n
        while head:
            while s and head.val > s[-1][0]:
                r[s.pop()[1]] = head.val
            s.append((head.val, i))
            i += 1
            head = head.next
        return r
