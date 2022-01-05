# python_repository_simple

本リポジトリはシンプルな Python 環境のテンプレートリポジトリです
devcontainer の設定をしていますので、VS Code と Docker、Git さえあれば各種開発用設定が行われた Python の開発環境が構築され、即時開発が可能です
GitHub のリポジトリページの「Use this template」を押下して使用してください

## 内容

- [devcontainer](https://code.visualstudio.com/docs/remote/containers)
- lint
  - [flake8](https://flake8.pycqa.org/en/latest/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), [pyright](https://github.com/microsoft/pyright)
  - [hadolint](https://github.com/hadolint/hadolint)
- [pytest](https://docs.pytest.org/en/stable/)
- [poetry](https://python-poetry.org/)
- [GitHub Actions](https://github.co.jp/features/actions)
- [logging](https://docs.python.org/ja/3/howto/logging.html)

## 環境詳細

- Python : 3.9

### 事前準備

- Docker インストール
- VS Code インストール
- VS Code の拡張機能「Remote - Containers」インストール
  - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
- 本リポジトリの clone
- `.env` ファイルを空ファイルでプロジェクト直下に作成
- 以下をプロジェクト名に合わせて変更
  - `.devcontainer/devcontainer.json`
    - `name`, `service`
  - `docker-compose.yml`
    - `services` の Key 名
    - `image`, `container_name`
    - `env_file`
      - 環境変数を使用しない場合は除去
  - main.py
  - logging.conf
    - `hoge` を使用するモジュール名に合わせる
  - `README.md`
  - `LICENSE`
  - dependabot
    - `.github/dependabot.yml`
    - `.github/workflows/auto_merge_depandabot.yml`
  - pyproject.toml
    - `tool.poetry.name`, `tool.poetry.description`, `tool.poetry.authors`

### 開発手順

1. VS Code 起動
2. 左下の緑色のアイコンクリック
3. 「Remote-Containersa: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナー image の取得や作成が行われる
5. 起動したら開発可能

## ユニットテスト実行

```
pytest
```
