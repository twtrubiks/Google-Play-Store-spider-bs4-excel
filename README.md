# Scrapy-Google-Play-Store-bs4-excel
抓取 [Google Play Store](https://play.google.com/store/apps/top) 資料 use [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) on Python 📝  

並使用 SQLite 儲存 DB 以及 EXCEL

* [Youtube Demo]()   


## 特色
* 透過 [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 抓取 [Google Play Store](https://play.google.com/store/apps/top) 資料 (熱門排行榜) 前100筆資料。
* 使用 SQLITE 儲存資料。
* 使用 [pyexcel](https://github.com/pyexcel/pyexcel) 將資料轉為 Excel。
* example 資料夾底下，有我自己寫的簡單 [pyexcel](https://github.com/pyexcel/pyexcel) 範例，分別為 DB -> EXCEL ( [SQL_Database_To_Excel.py]() ) 以及 EXCEL -> DB ( [Excel_To_SQL_Database.py]() ) 
   
   



## 安裝套件 
確定電腦有安裝 [Python](https://www.python.org/) 之後

clone 我的簡單範例

``` 
git clone https://github.com/twtrubiks/Google-Play-Store-spider-bs4-excel.git
```

接著請在  cmd (命令提示字元) 輸入以下指令
``` 
pip install -r requirements.txt
```

## 使用方法 以及 執行畫面

抓取 [Google Play Store](https://play.google.com/store/apps/top) 資料 (熱門排行榜 最新發佈) 前100筆資料。

``` 
python app.py
```
執行畫面

![alt tag](http://i.imgur.com/B7hrB4z.png)

![alt tag](http://i.imgur.com/1qlcCtT.png)

![alt tag](http://i.imgur.com/by1458l.png)


執行完畢後，會將資料存在 app.db 裡，可以使用 [SQLiteBrowser](http://sqlitebrowser.org/) 觀看

![alt tag](http://i.imgur.com/GdhGZcp.png)

Item 欄位總共會有 6 個類型，分別為

<b>Android 應用程式類熱門免費下載 </b>、<b>Android 應用程式類熱門付費下載</b>、<b>Android 應用程式類最賣座項目</b>、

<b>遊戲類熱門免費下載</b>、<b>遊戲類熱門付費下載</b>、<b>遊戲類最賣座項目</b>

每種類別各 100 筆資料，每執行一次 <b>app.py</b> ，就會有 600 筆資料 (除非資料有問題)


如果你需要將資料存成 EXCEL 

可以再執行
``` 
python SQL_Database_To_Excel.py
```
執行完畢後，會多出名稱為 <b>Excel-data.xlsx</b>

![alt tag](http://i.imgur.com/gxt7YTl.jpg)



## 執行環境
* Python 3.4.3

## Reference 
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 
* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [pyexcel](https://github.com/pyexcel/pyexcel)
* [pyexcel_xlsx](https://github.com/pyexcel/pyexcel-xlsx)
* [requests](http://docs.python-requests.org/en/master/)


## License
MIT license
