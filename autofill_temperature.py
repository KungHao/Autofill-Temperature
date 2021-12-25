from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

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

if __name__ == "__main__":    
    IDs = ["127727","123843","125800","127744", "122908"]
    # IDs = ['125800']

    for i in IDs:
        temp = temperatureGen()
        fill(i, temp)
        current_time = get_now()
        print('ID: ', i)
        print("temp: ", temp)
        print("Current Time =", current_time)
