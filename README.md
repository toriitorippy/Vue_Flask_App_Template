# Vue_Flask_App_Template

## 説明
Vue+Flaskで構成されたDocker環境で動くSPAのアプリの個人的なテンプレートです。
あるシステムのプロトタイプを作成した時のベースとして使用しました。
Azureにデプロイする時用にdeployブランチを用意しています。

※Azureのデプロイする手順を記したQiita記事を書きました。
[Vue+Flask on DockerのWebアプリケーションをAzureにデプロイする]()

## コンテナ立ち上げ

vueのパッケージインストール
※node_modulesとyarn.lockがない状態か確認
```
docker-compose run vue yarn
```

vueとflaskのbuild
```
docker-compose build
```

docker立ち上げ
```
docker-compose up vue
```

frontendは　[http://localhost:8080/](http://localhost:8080/)　にアクセス

api側は　[http://localhost:5000/](http://localhost:5000/)　にアクセスする。例えば、[http://localhost:5000/rand](http://localhost:5000/rand)　のようにjson形式を返すことができる。フロントはこのエンドポイントを用いてデータをバックエンドから受け取る。


## 参考サイト
環境構築するのに参考にしたサイト

[vue+docker](https://qiita.com/rh_taro/items/ca08b930f704275286a4)

[flask](https://qiita.com/rockguitar67/items/f8edc33dd221d8f4e965)

