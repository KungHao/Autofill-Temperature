import time
import random
from datetime import datetime
from selenium import webdriver
from flask import Flask, request, abort
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import *


# James Function
IDs = ["127727","123843","125800","127744", "122908"]
# IDs = ['125800']

def fill(empid, temp):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # browser = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=options)
    # browser = webdriver.Chrome('D:/Github/Autofill-Temperature/chromedriver/chromedriver.exe', options=options)

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
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
    res = 'ID: ' + id + "\nTemperature: " + str(temp) + "\nTime: " + current_time
    return res

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
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # print("event.reply_token:", event.reply_token)
    # print("event.message.text:", event.message.text)
    if event.message.text == 'Tsmc':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='Done!!!'))
        for i in IDs:
            res = main(i)
            print(res)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=res))
        return 0
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
        return 0


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
