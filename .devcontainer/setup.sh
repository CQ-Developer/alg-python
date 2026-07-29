export http_proxy=http://172.31.112.1:7890
export https_proxy=http://172.31.112.1:7890

curl -LsSf https://astral.sh/uv/install.sh | sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash
curl -s "https://get.sdkman.io" | bash
