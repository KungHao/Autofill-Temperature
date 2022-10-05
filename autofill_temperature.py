import time
import random
from send_notify import *
from datetime import datetime, timezone, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def fill(empid):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get('https://zh.surveymonkey.com/r/EmployeeHealthCheck')

    radioBtn = browser.find_elements(By.CLASS_NAME, "radio-button-display")
    radioTxt = browser.find_elements(By.CLASS_NAME, "radio-button-label-text")
    textbox = browser.find_elements(By.CLASS_NAME, "wds-input")
    checkbox = browser.find_elements(By.CLASS_NAME, "checkbox-button-display")
    radioBtn_checked = [0, 4, 8, 9]


    for i in radioBtn_checked:
        # print(radioTxt[i].text)
        radioBtn[i].click()

    # checkbox[0].click()
    # info = [empid, temp]
    info = [empid]

    for i in range(len(textbox)):
        textbox[i].send_keys(str(info[i]))

    time.sleep(2)

    browser.find_elements(By.CLASS_NAME, "next-button")[0].click()
    done = browser.find_elements(By.XPATH, "//span[contains(text(),'You have completed!')]")

    browser.close()
    return done

def temperatureGen():
    return round(random.uniform(35.6, 37.1), 1)

def get_now():
    now = datetime.now()
    now = now.astimezone(timezone(timedelta(hours=8)))
    current_time = now.strftime("%H:%M:%S")
    return current_time

def check_result(res) -> str:
    if len(res) == 0:
        return "失敗"
    else:
        return "成功"

if __name__ == "__main__":    
    # IDs = ["123843", "127727", "127744", "122908", '125916', '066763', '116282', '121713', '125897', '115697']
    IDs = ['125800', '123843', '127727', '127744']

    for ID in IDs:
        # temp = temperatureGen()
        res = fill(ID)
        current_time = get_now()
        result = check_result(res)
        line_reply = f"\nResult: {result}\nID: {ID} \nTime: {current_time}"
        print(line_reply)
        # print('ID: ', ID)
        # print("temp: ", temp)
        # print("Current Time :", current_time)
        # print("Result: ", result)
        lineNotifyMessage('196YlNGoW1ufiDV71VhFzP1SzirT2Xls2Tz6PNSYyR7', line_reply)

