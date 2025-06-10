# alg-python

## setup venv

```shell
python -m venv .venv
pipenv install sortedcontainers sortedcontainers-stubs
```

## create __init__.py

```shell
find src/ -type f -exec touch "{}/__init__.py" \;
find test/ -type f -exec touch "{}/__init__.py" \;
```

## vscode config

```json
{
    "black-formatter.args": [
        "-S",
        "-l", "999"
    ],
    "python.analysis.typeCheckingMode": "strict",
    "python.analysis.extraPaths": [
        "src",
        "test"
    ],
    "python.analysis.diagnosticSeverityOverrides": {
        "reportIncompatibleMethodOverride": "warning"
    },
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-t", ".",
        "-s", "test",
        "-p", "test_*.py"
    ],
    "python.terminal.activateEnvironment": true,
    "python.defaultInterpreterPath": ".venv/bin/python"
}
```
