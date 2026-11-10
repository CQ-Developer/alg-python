import pytest

from src.n3709 import ExamTracker, ExamTrackerA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[ExamTrackerA])
def exam_tracker_cls(request: pytest.FixtureRequest) -> type[ExamTracker]:
    return request.param


@pytest.mark.parametrize("case", load_cases(__file__))
def test_exam_tracker(exam_tracker_cls: type[ExamTracker], case: Case):
    exam_tracker = exam_tracker_cls(*case["init"])
    actual = [
        getattr(exam_tracker, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
