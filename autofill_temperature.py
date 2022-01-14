import time
import random
from send_notify import *
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
    radiobutton_checked = [0,1,5,6,9,10]

    for i in radiobutton_checked:
        radiobutton[i].click()

    checkbox[0].click()
    info = [empid, temp]

    for i in range(len(textbox)):
        textbox[i].send_keys(str(info[i]))

    time.sleep(2)

    browser.find_elements_by_class_name("btn")[0].click()
    browser.close()

def temperatureGen():
    return round(random.uniform(35.6, 37.1), 1)

def get_now():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

if __name__ == "__main__":    
    IDs = ["123843", "127727", "127744", "122908", '125916', '066763', '116282', '121713', '125897', '115697']

    for i in IDs:
        temp = temperatureGen()
        fill(i, temp)
        current_time = get_now()

        res = '\nID: ' + i + "\nTime: " + current_time + "\nTemperature: " + str(temp)
        print('ID: ', i)
        print("temp: ", temp)
        print("Current Time =", current_time)
        lineNotifyMessage('196YlNGoW1ufiDV71VhFzP1SzirT2Xls2Tz6PNSYyR7', res)
