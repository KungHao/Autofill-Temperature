---
title: 'Heroku建置教學'
disqus: hackmd
---

## Heroku 建置過程

[TOC]

## 必要檔案

(1) Procfile  --> 告訴 Heroku 如何啟動程式

```web: python app.py```

(2) requirements.txt  --> 告訴 Heroku 要安裝哪些套件
```
flask
selenium
line-bot-sdk
webdriver_manager
```
(3) app.py  --> 主程式

(4) runtime.txt  --> 要執行程式的 Python 版本

`python-3.7.10`

建置流程
---

建置完檔案後進行首次Deploy，透過Heroku Git Deploy
(Install the Heroku CLI, before deploy)
https://devcenter.heroku.com/articles/heroku-command-line

登入Heroku
```
$ heroku login
```
Clone the repository
```
heroku git:clone -a app_name 
cd autofill-temperature
```
Deploy changes
```
git add .
git commit -am "make it better"
git push heroku master
```

定時執行程式 Heroku Scheduler
---
若是要用 Heroku Scheduler必須要登記信用卡資訊

* Schedule: 設定run code時間
1. 於Resource的頁面點擊Find more add-ons
2. 搜尋Heroku Scheduler
3. add jobs，這邊要注意schedule只有三種設置
    * Every 10 minutes
    * Every hour at ...
    * Every dat at ...
若要於特定時間就要在de裡面自行判斷時間。
* Run Command: 設定要執行的語法
`$ python app.py`

**要特別注意在這裡的時間是UTC+0，台灣時間是UTC+8，要自行轉換**

Selenium爬蟲特例
---
由於selenium需要有path設定，所以必須自行加上Configuration。
在Settings的頁面於Config Vars和Buildpacks加上config。

![設定檔圖片](https://i.imgur.com/pzCcZxW.png)

## Appendix and FAQ

* 若要同時push heroku, github必須設定兩個remote

###### tags: `Heroku` `Heroku Scheduler`
