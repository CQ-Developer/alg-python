# Test case format

Every `tests/test_nXXX.py` module loads its data from
`tests/cases/nXXX.json` through `tests.case_loader.load_cases`.
The `test_` prefix is removed from the test module name to form the case file
name.

`load_cases` returns `Case` objects whose values are deep-copied on access, so
in-place solutions cannot mutate the shared case data between solution
variants.

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
