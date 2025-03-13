## Django アプリ（Django）

### コマンド

- 起動  
  `python3 manage.py runserver`

- Shell コマンド  
  `python manage.py shell`

## DB（Ecommerce）

MySQL を使用。

### コマンド

- マイグレート  
  `python3 manage.py migrate`

- 商品の追加  
  fixtures の JSON ファイルに追加して、  
  `python3 manage.py loaddata <fixturesのJSONファイル名>`

- ログイン  
  `mysql -u root -p`  
  または  
  `sudo mysql -u root`
- DB アクセス  
   mysql>  
   `USE ECommerce;`

- テーブル一覧表示  
  mysql>  
   `SHOW TABLES;`

- テーブルカラム表示  
  mysql>  
  `SHOW COLUMNS FROM <テーブル名>;`

- テーブルデータ表示  
   mysql>
  `SELECT * FROM <テーブル名>;`

- テーブルデータ削除（オートインクリメントもリセット）  
  mysql>  
  `TRUNCATE TABLE shop_product;`

- テーブルデータ削除（オートインクリメントはそのまま）  
  mysql>  
  `DELETE FROM shop_product;`

- 退出  
  mysql>  
   `exit`
