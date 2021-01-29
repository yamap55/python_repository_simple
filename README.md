# python_repository_simple

本リポジトリはシンプルな Python 環境のテンプレートリポジトリです
devcontainer の設定をしていますので、VSCode と Docker、Git さえあれば各種開発用設定が行われた Python の開発環境が構築され、即時開発が可能です
GitHub のリポジトリページの「Use this template」を押下して使用してください

## 内容

- devcontainer
- lint
  - flake8, black, pyright
- pytest
- GitHub Actions
- logging

## 環境詳細

- Python : 3.8.7

### 事前準備

- Docker インストール
- VSCode インストール
- VSCode の拡張機能「Remote - Containers」インストール
  - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
- 本リポジトリの clone
- `.env` ファイルを空ファイルでプロジェクト直下に作成
- 以下をプロジェクト名に合わせて変更
  - `.devcontainer/devcontainer.json`
    - `name`, `service`
  - `docker-compose.yml`
    - `services` の Key 名
    - `image`, `container_name`
  - main.py
  - logging.conf
    - `hoge` を使用するモジュール名に合わせる
  - `README.md`
  - `LICENSE`

### 開発手順

1. VSCode 起動
2. 左下の緑色のアイコンクリック
3. 「Remote-Containersa: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナ image の取得や作成が行われる
5. 起動したら開発可能

## ユニットテスト実行

```
pytest
```
