# scrapeTwitter--selenium-python-描述及用法:
面對關心及更新較快的用戶更新內容，可以以此工具快速觀看推文回覆或是使用推文翻譯功能。
此腳本將搜尋特定推特用戶名時間軸上前三則推文，儲存至log文字檔，並以預設瀏覽器分頁分別自動開啟此三則推文。無須登入或使用依賴twitter的工具
    
    $echo <username>|python scrape.py 例如 $echo TIME|python scrape.py
    或
    $python scrape.py之後，待出現詢問句，再輸入<username>+enter

# 運行環境:
  * Ubuntu 20.04 
  * selenium 4.6.0
  * geckodriver 0.32.2
  * python 3.10.6


# 其他建議:
  * $for i in range(3):中，(3)可改成其他有興趣的範圍，用法請參考python的range()函數
# 實際結果:

![image](https://github.com/k-eeer/scrapeTwitter--selenium-python/blob/main/demo.png)

使用者輸入用戶名後將自動打開時間軸上前三則推文，並將推文的時間跟url寫入tweeter.log

若使用echo 提前輸入選擇，可略過詢問訊息，等待瀏覽器自動打開分頁
