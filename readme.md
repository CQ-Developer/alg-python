# alg-python

## setup venv

```shell
uv sync
```

## vscode config

```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true
    },
    "black-formatter.args": [
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
    "remoteUser": "chen",
    "remoteEnv": {
        "TZ": "Asia/Shanghai",
        "Lang": "C.UTF-8"
    },
    "build": {
        "dockerfile": "Dockerfile"
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-python.black-formatter",
                "tamasfe.even-better-toml"
            ]
        }
    }
}
```

```dockerfile
FROM docker.1ms.run/library/fedora:43
RUN sed -i \
        -e 's|^metalink=|#metalink=|g' \
        -e 's|^#baseurl=http://download.example/pub/fedora/linux|baseurl=https://mirrors.tuna.tsinghua.edu.cn/fedora|g' \
        /etc/yum.repos.d/fedora.repo /etc/yum.repos.d/fedora-updates.repo && \
    dnf -y upgrade && \
    dnf -y install git curl zip unzip && \
    groupadd -g 1000 chen && \
    useradd -m -s /bin/bash -u 1000 -g 1000 chen
WORKDIR /home/chen
COPY init.sh .
RUN chown 1000:1000 init.sh && \
    chmod 754 init.sh
USER chen
RUN ./init.sh
```

```shell
#!/bin/bash
curl -LsSf https://astral.sh/uv/install.sh | sh
rm -f ./init.sh
```