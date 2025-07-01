from abc import ABC, abstractmethod


def is_bad_version(version: int) -> bool:
    return False


class Solution(ABC):

    @abstractmethod
    def first_bad_version(self, n: int) -> int:
        pass
