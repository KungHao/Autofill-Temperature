---
title: 'Auto-Fill Temperature'
---

Auto-fill Temperature
===

## Table of Contents

[TOC]

## Beginners Guide

1. 新增工號於IDs
2. 填入Line Notify Token
3. 到Heroku Scheduler設定執行時間

手動新增工號於autofill_temperature.py

lineNotifyMessage(token, res)填入line notify的token

> Line Notify URL: https://notify-bot.line.me/
> Heroku: https://dashboard.heroku.com/

## 必要檔案

若是有callback則需要Procfile

(1) Procfile  --> 告訴 Heroku 如何啟動程式

```web: python app.py```

(2) requirements.txt  --> 告訴 Heroku 要安裝哪些套件
```
flask
selenium
line-bot-sdk
webdriver_manager
```
(3) app.py  --> Line Chatbot 主程式

(4) runtime.txt  --> 要執行程式的 Python 版本

`python-3.7.10`

###### tags: `Heroku` `line-chatbot`
