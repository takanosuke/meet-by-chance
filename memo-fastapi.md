

# コマンドメモ

* モジュールのインストール
  * pip install fastapi
  * pip install uvicorn
* ドキュメント
  * 対話的APIドキュメントを表示（SwaggerUI)
    * http://127.0.0.1:8000/docs
  * 対話的APIドキュメントを表示（ReDoc)
    * http://127.0.0.1:8000/redoc

* サーバ起動
  * uvicorn {ファイル名}:{インスタンスが入った変数名} --reload
    * uvicorn main:app --reload
    * `main`: `main.py`ファイル (Python "モジュール")
    * `app`: `main.py` の`app = FastAPI()`の行で生成されたオブジェクト
    * `--reload`: コードを変更したらサーバーを再起動します。このオプションは開発環境でのみ使用します
* uvicorn

`uvicorn main:app`コマンドは以下の項目を参照します:

- `main`: `main.py`ファイル (Python "モジュール")
- `app`: `main.py` の`app = FastAPI()`の行で生成されたオブジェクト
- `--reload`: コードを変更したらサーバーを再起動します。このオプションは開発環境でのみ使用します



# メモ

* Enumを継承したクラスを使って固定値を再現し、それを型アノテーションとすることでパラメータの値を制限する
* パラメータにパスを指定する場合は、/files/{file_path:path}でアノテーションする。また、パスは戦闘がスラッシュである必要がある
* Pydanticモデルで宣言されたパラメータはリクエストボディとして受け取る。（BaseModelを継承したクラス）
* クエリパラメータのバリデーションはQueryを使う。
  * 必須にしたいときは、q: str = Query(..., max_length={上限値})
  *  q: str = Query({初期値}, max_length={上限値})

* パスパラメータのバリデーションはPathを使う
  * パスパラメータは必須なので初期値は...とする。適当な値を入れてても問題ないけど意味ない
  * p: str = Path(..., max_length={上限値})

* ボディを明示的にするためにはBodyを使う
  * Item: Item = Body(..., embed=True)
  * embed=Trueがあると、単一のボディでもキー付きでくることを期待する
