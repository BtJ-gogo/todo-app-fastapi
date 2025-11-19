# TodoApp (FastAPI 学習用)

FastAPI を学習するために作成したシンプルな Todo API です。

## 使用技術
- FastAPI
- SQLite (開発用)
- SQLAlchemy

## APIエンドポイント
| メソッド | パス | 内容 |
|-----------|------|------|
| GET | /api/tasks | タスク一覧取得 |
| POST | /api/tasks | 新規作成 |
| GET | /api/tasks/{id} | タスク詳細 |
| PATCH | /api/tasks/{id} | 編集 |
| DELETE | /api/tasks/{id} | 削除 |
