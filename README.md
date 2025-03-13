## Django アプリ（Django）

### コマンド

- 起動  
  `python3 manage.py runserver`

## DB（Ecommerce）

MySQL を使用。

### コマンド

- マイグレート  
  `python3 manage.py migrate`

- 商品の追加  
  initial_data.json に追加して、  
  `python3 manage.py loaddata initial_data.json`

- ログイン  
  `sudo mysql -u root`  
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

- 退出  
  mysql>  
   `exit`
