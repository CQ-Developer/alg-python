from abc import ABC, abstractmethod


class MountainArray(ABC):

    @abstractmethod
    def get(self, index: int) -> int:
        pass

    @abstractmethod
    def length(self) -> int:
        pass


class Solution(ABC):

    @abstractmethod
    def find_in_mountain_array(self, target: int, mountainArr: MountainArray) -> int:
        pass
