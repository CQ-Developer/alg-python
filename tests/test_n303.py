import pytest

from src.n303 import NumArray
from tests.case_loader import Case, load_cases


@pytest.mark.parametrize("case", load_cases(__file__))
def test_num_array(case: Case):
    num_array = NumArray(*case["init"])
    actual = [
        getattr(num_array, operation)(*arguments) for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
