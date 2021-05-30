


# コマンドメモ
* マイグレーションファイルの作成
  * python manage.py makemigrations {app名}

* migrateした場合に発行されるSQLの確認
  * python manage.py sqlmigrate {app名} {migrate番号}

* migrate実行
  * python manage.py migrate {app名}

* 既存のDBを読み込んでmodel.pyのコードを返す
  * python manage.py inspectdb

* サーバー起動
  * python manage.py runservert

# プロジェクト開始とアプリ作成
* pip install django, django-cors-headers django-filter djangorestframework
* django-admin startproject server
* django-admin startapp image
* settingsのappにimageを追加

# DB接続のためにやること
* mysql接続用のモジュールインストール
  * pip install mysqlclient
* 接続先DBの設定をsettings.pyに記述
* 既存のDBに接続するなら、model.pyに既存DBの情報を記述
  * python manage.py inspectdb
* 新規のDBに接続するなら、model.pyにテーブル情報を書く
* マイグレーションファイルの作成
  * python manage.py makemigrations {app名}
* migrateの実行
  * python manage.py migrate {app名}

# 管理者ページ関連でやること
* userテーブルを作成する
  * python manage.py migrate
* 管理者ユーザ作成
  * python manage.py createsuperuser
* 管理者ページで扱いたいモデルを各appのadmin.pyに記述
    from .models import {modelのclass名}
    admin.site.register({modelのclass名})
* サーバを立てて、/adminにアクセス
  
# cors設定
* cors-headersのモジュールをインストール
  * pip install django, django-cors-headers
* settings.pyに設定を入れる
    INSTALLED_APPS = ['corsheaders']
    MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] # CommonMiddleWareより上に挿入
    CORS_ORIGIN_WHITELIST = ['localhost:4200',]
    CORS_ALLOW_CREDENTIALS = True
