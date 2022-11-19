# BookReadBolog

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

### Result


