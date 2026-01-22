#!/bin/bash

export http_proxy=http://172.17.0.1:10810
export https_proxy=http://172.17.0.1:10810

curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.11 --default

rm -f ./init.sh
