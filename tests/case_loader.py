import copy
import json
from pathlib import Path
from typing import Any


class Case(dict[str, Any]):
    """A JSON case that returns fresh values, so in-place solutions cannot leak state."""

    def __getitem__(self, key: str) -> Any:
        return copy.deepcopy(super().__getitem__(key))


def load_cases(module_file: str) -> list[Case]:
    """Load the JSON cases file that matches the calling test module."""
    case_name = Path(module_file).stem.removeprefix("test_")
    case_file = Path(module_file).parent / "cases" / f"{case_name}.json"
    return [Case(item) for item in json.loads(case_file.read_text(encoding="utf-8"))]
