## 概要

scraping と db へのデータのやりとりを行うプロジェクト(練習) \

scraping は selenium で XHR を解析、json を取得する。
selenium を使用するときに cloudfunctions

## ファイルの役割

### setup.py

ローカルで開発環境を立ち上げるためのファイル(優先度低)

### config.py

環境変数の整理

### main.py

todo

### 実行について

実行するときは最上位の main.py に import してから使うか、特定の dir で py を実行したい(debug 時)ときは \
`if __name__ == __main__`と`if __name__ != __main__`を使って ModuleNotFoundError が発生しないようにする。
