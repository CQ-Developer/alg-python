# alg-python

## setup venv

```shell
uv sync
```

## vscode config

```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "black-formatter.args": [
        "-S",
        "-l", "999"
    ],
    "python.analysis.typeCheckingMode": "standard",
    "python.analysis.extraPaths": [
        "src",
        "test"
    ],
    "python.analysis.diagnosticSeverityOverrides": {
        "reportIncompatibleMethodOverride": "warning",
        "reportUnknownLambdaType": "warning",
        "reportOptionalMemberAccess": "warning"
    },
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-t", ".",
        "-s", "test",
        "-p", "test_*.py"
    ],
    "python.terminal.activateEnvironment": true
}
```

## devcontainer config

```json
{
    "name": "alg-python",
    "build": {
        "dockerfile": "Dockerfile"
    },
    "features": {
        "ghcr.io/devcontainers/features/python:1": {
            "version": "none",
            "installTools": false,
            "optimize": true
        },
        "ghcr.io/devcontainers/features/common-utils:2": {
            "upgradlePackages": true,
            "installOhMyZsh": false,
            "installOhMyZshConfig": false,
            "installZsh": false
        }
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.black-formatter"
            ]
        }
    }
}
```

```dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.12
USER vscode
WORKDIR /home/vscode
RUN wget -qO- https://astral.sh/uv/install.sh | sh
```
