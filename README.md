# BookReadBolog

## API Data

[API仕様の概要 « 国立国会図書館サーチについて](https://iss.ndl.go.jp/information/api/riyou/)

[APIのご利用について « 国立国会図書館サーチについて](https://iss.ndl.go.jp/information/api/)

[国立国会図書館サーチの検索API(SRU)を使う - エイエイレトリック](https://eieito.hatenablog.com/entry/2019/09/12/220027)

[附録3（インタフェース仕様書）-国立国会図書館サーチ](https://iss.ndl.go.jp/information/wp-content/uploads/2022/07/ndlsearch_api_ap3_20220713.pdf)

[国会図書館サーチ ＡＰＩ で書籍情報をまとめて取得－python | コード７区](http://ailaby.com/ndl_search/)

[インターフェース仕様書(第2.2版)](https://iss.ndl.go.jp/information/wp-content/uploads/2022/05/ndlsearch_api_20220520_jp.pdf)

## ToDo

- 値段がないときの処理を行う。

APIの結果で値段の項目がないものがある。
現状は以下のエラーを出すようにしている。

"price": item['dcndl:price'],
KeyError: 'dcndl:price'

テストデータ
APIMain("エンジニアリングマネージャーのしごと")


### plan

- デフォルト値を入れる
- 値段があるAPIデータの種別を探す
- 取ってくるAPIを制限する

### Memo

- APIの順番が物によって異なっている
  - APIのItemによってデータが異なる
  - 推測：いろいろな書庫？のデータを取ってきているのでほしいところだけに絞る

### Result


