# Vue_Flask_App_Template

## 説明
後ほど記述

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

api側は　[http://localhost:5000/](http://localhost:5000/)　にアクセスする。例えば、[http://localhost:5000/](http://localhost:5000/)　のようにjson形式を返すことができる。フロントはこのエンドポイントを用いてデータをバックエンドから受け取る。

## 参考サイト
環境構築するのに参考にしたサイト

[vue+docker](https://qiita.com/rh_taro/items/ca08b930f704275286a4)

[nginx+docker](https://qiita.com/69incat/items/9bbfbf8566535dc266c6)

[flask](https://qiita.com/rockguitar67/items/f8edc33dd221d8f4e965)

[mongo](https://qiita.com/mistolteen/items/ce38db7981cc2fe7821a)