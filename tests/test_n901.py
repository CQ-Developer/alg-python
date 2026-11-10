import copy
import json
from pathlib import Path
from typing import Any, TypedDict

import pytest

from src.n901 import StockSpanner, StockSpannerA


class Case(TypedDict):
    init: list[Any]
    operations: list[str]
    arguments: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n901.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[StockSpannerA])
def stock_spanner_cls(request: pytest.FixtureRequest) -> type[StockSpanner]:
    return request.param


@pytest.mark.parametrize("case", _load_test_cases())
def test_stock_spanner(stock_spanner_cls: type[StockSpanner], case: Case):
    case = copy.deepcopy(case)
    stock_spanner = stock_spanner_cls(*case["init"])
    actual = [
        getattr(stock_spanner, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
