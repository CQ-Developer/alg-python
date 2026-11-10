# Test case format

Each `tests/test_nXXX.py` module is self-contained:

- it defines its own `TestCase(TypedDict)`
- it defines its own `_load_test_cases()` and reads `tests/cases/nXXX.json`
- it deep-copies the case before using it
- it defines any tree/list helpers it needs

The `test_` prefix is removed from the test module name to form the case file
name. `TestCase` sets `__test__ = False` so pytest does not try to collect it as
a test class.

## Regular problems

Each item in the top-level array is one test case. Keys are the parameter
names of the solution method, followed by `expected`:

```json
[
  {
    "nums": [2, 7, 11, 15],
    "target": 9,
    "expected": [0, 1]
  }
]
```

## Design problems

Design problems use a constructor argument list and an operation trace:

```json
[
  {
    "init": [[-2, 0, 3, -5, 2, -1]],
    "operations": ["sum_range", "sum_range", "sum_range"],
    "arguments": [[0, 2], [2, 5], [0, 5]],
    "expected": [1, -1, -3]
  }
]
```

## Trees and linked lists

Trees use LeetCode level-order arrays with `null` for missing children.
Trailing `null` values are trimmed. Linked lists use plain arrays.

```json
[
  {
    "root": [1, 2, 3, null, null, 4, 5],
    "expected": 6
  }
]
```

## Multiple valid answers

Use `expected_any` when the problem accepts more than one answer:

```json
[
  {
    "nums": [1, 2, 1, 3, 5, 6, 4],
    "expected_any": [1, 5]
  }
]
```
