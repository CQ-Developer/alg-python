import pytest

from src.n3709 import ExamTracker, ExamTrackerA


@pytest.fixture(params=[ExamTrackerA])
def exam_tracker_cls(request: pytest.FixtureRequest) -> type[ExamTracker]:
    return request.param


@pytest.mark.parametrize(
    [
        "targets",
        "params",
        "expected",
    ],
    [
        pytest.param(
            [
                "ExamTracker",
                "record",
                "total_score",
                "record",
                "total_score",
                "total_score",
                "total_score",
                "total_score",
            ],
            [
                [],
                [1, 98],
                [1, 1],
                [5, 99],
                [1, 3],
                [1, 5],
                [3, 4],
                [2, 5],
            ],
            [
                None,
                None,
                98,
                None,
                98,
                197,
                0,
                99,
            ],
        ),
    ],
)
def test_exam_tracker(
    exam_tracker_cls: type[ExamTracker],
    targets: list[str],
    params: list[list[int]],
    expected: list[int | None],
):
    exam_tracker = exam_tracker_cls()
    assert [getattr(exam_tracker, t)(*p) for t, p in zip(targets[1:], params[1:])] == expected[1:]
