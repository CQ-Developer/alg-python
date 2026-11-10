import copy
import json
from pathlib import Path
from typing import Any, TypedDict

import pytest

from src.n3709 import ExamTracker, ExamTrackerA


class TestCase(TypedDict):
    __test__ = False
    init: list[Any]
    operations: list[str]
    arguments: list[list[int]]
    expected: list[int | None]


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[ExamTrackerA])
def exam_tracker_cls(request: pytest.FixtureRequest) -> type[ExamTracker]:
    return request.param


@pytest.mark.parametrize("case", _load_test_cases())
def test_exam_tracker(exam_tracker_cls: type[ExamTracker], case: TestCase):
    case = copy.deepcopy(case)
    exam_tracker = exam_tracker_cls(*case["init"])
    actual = [
        getattr(exam_tracker, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
