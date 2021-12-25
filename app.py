import time
import random
from datetime import datetime
from selenium import webdriver
from flask import Flask, request, abort
from selenium.webdriver.chrome.options import Options
from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import *

# James Function
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

# IDs = ["127727","123843","125800","127744", "122908"]
IDs = ['125800']

def fill(empid, temp):
    browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
    browser.get('https://zh.surveymonkey.com/r/EmployeeHealthCheck') 

    radiobutton = browser.find_elements_by_class_name("radio-button-display")

    textbox = browser.find_elements_by_class_name("wds-input")

    checkbox = browser.find_elements_by_class_name("checkbox-button-display")

    radiobutton_checked = [0,1,5,6,8]

    for i in radiobutton_checked:
        radiobutton[i].click()

    checkbox[0].click()
    info = [empid, temp]

    for i in range(len(textbox)):
        textbox[i].send_keys(str(info[i]))

    time.sleep(1)

    browser.find_elements_by_class_name("btn")[0].click()
    browser.close()

def temperatureGen():
    return round(random.uniform(35.6, 37.3), 1)

def get_now():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def main(id):
    temp = temperatureGen()
    fill(id, temp)
    current_time = get_now()
    print('ID: ', id)
    print("Temperature: ", temp)
    print("Time: ", current_time)
    return  str('ID: ' + id + "\nTemperature: " + temp + "\nTime: " + current_time)

app = Flask(__name__)

# LINE_BOT_API, HANDLER = getConfig()
# line_bot_api = LineBotApi(LINE_BOT_API)
# handler = WebhookHandler(HANDLER)

line_bot_api = LineBotApi('EJSVqZ3qRoLdcUWDqhToDwfkIhO8dUMPVPyymuNeCXYGeAhR5AhiUehZgVjvGZOMXJyhwibw5Q17zmRfjw3O73jJahGAirpZ6+jbIHrXR/dsCxmskLBSZgCtlV1V/JEIX8XtEvx4Kyq5OOgBHx3sUAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1f93d9addae9280fe895704ac511c425')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # print("event.reply_token:", event.reply_token)
    # print("event.message.text:", event.message.text)
    if event.message.text == 'Test':
        for i in IDs:
            res = main(i)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=res)
                )
        return 0
    # if event.message.text.lower() == "":
    #     content = ptt_hot()
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=content))
    #     return 0
    # elif event.message.text.lower() == 'show':
    #     flex_send_message = FlexSendMessage(
    #             alt_text='alt_text',
    #             contents={
    #                 'type':'bubble',
    #                 'header':{
    #                     'type':'box',
    #                     'layout':'vertical',
    #                     'contents':
    #                         [
    #                             {
    #                                 "type": "text",
    #                                 "text": "Choose one",
    #                                 "weight": "bold",
    #                                 "align": "center"
    #                             },
    #                             {
    #                                 "type": "separator",
    #                                 "color": "#000000",
    #                                 "margin": "xxl"
    #                             }
    #                         ]
    #                 },
    #                 "body": {
    #                     "type": "box",
    #                     "layout": "vertical",
    #                     "contents": [
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "Lifeismoney",
    #                                 "text": "Lifeismoney"
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "Stock",
    #                                 "text": 'Stock'
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "Tech_Job",
    #                                 "text": 'Tech_Job'
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "科技新報",
    #                                 "text": '科技新報'
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "Sex",
    #                                 "text": 'Sex'
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "NSwitch",
    #                                 "text": 'NSwitch'
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "Beauty",
    #                                 "text": 'Beauty'
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "japanavgirls",
    #                                 "text": 'japanavgirls'
    #                             }
    #                         },
    #                         {
    #                             "type": "button",
    #                             "action": {
    #                                 "type": "message",
    #                                 "label": "Shu-Lin",
    #                                 "text": 'Shu-Lin'
    #                             }
    #                         }
    #                     ]
    #                 }
    #             }
    #         )
        
    #     line_bot_api.reply_message(event.reply_token, flex_send_message)
        
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
        return 0


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
