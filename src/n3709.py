import abc
import bisect
import typing


class ExamTracker(abc.ABC):
    @abc.abstractmethod
    def record(self, time: int, score: int):
        pass

    @abc.abstractmethod
    def total_score(self, start_time: int, end_time: int) -> int | None:
        pass


class ExamTrackerA(ExamTracker):
    def __init__(self) -> None:
        self.times = []
        self.scores = [0]

    @typing.override
    def record(self, time: int, score: int):
        self.times.append(time)
        self.scores.append(self.scores[-1] + score)

    @typing.override
    def total_score(self, start_time: int, end_time: int) -> int:
        l = bisect.bisect_left(self.times, start_time)
        r = bisect.bisect_right(self.times, end_time)
        return self.scores[r] - self.scores[l]
