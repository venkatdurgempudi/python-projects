#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

with open('D:/KiteAutomation/auth.json', 'r') as f:
    login = json.load(f)

username = login['user_id']
password = login['password']
totp = login['totp']
webdriver_path = login['webdriver_path']  # path of your chromedriver
url = login['url']

# launch chrome and open zerodha website

# pip install pyotp
# pip install -U selenium==4.11.2

from selenium import webdriver
from time import sleep
from pyotp import TOTP
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

print url

option = Options()

option.add_argument('--disable-infobars')
option.add_argument('start-maximized')
option.add_argument('--disable-extensions')

# Pass the argument 1 to allow and 2 to block

option.add_experimental_option('prefs',
                               {'profile.default_content_setting_values.notifications': 1})

driver = webdriver.Chrome(chrome_options=option,
                          executable_path=r"C:\Users\venka\chromedriver-win64\chromedriver.exe"
                          )

driver.get(url)
driver.maximize_window()

# input username

user = driver.find_element('xpath', "//input[@type = 'text']")
user.send_keys(username)

# input password

pwd = driver.find_element('xpath', "//input[@type = 'password']")
pwd.send_keys(password)

# click on login

driver.find_element('xpath', "//button[@type='submit']").click()

sleep(1)

# input totp

ztotp = driver.find_element('xpath', "//input[@type = 'number']")
totp_token = TOTP(totp)
token = totp_token.now()
ztotp.send_keys(token)

# click on continue

driver.find_element('xpath', "//button[@type = 'submit']").click()

sleep(5)

# click on "I Understand"
# driver.find_element("xpath","//button[@type = 'button' and @class='button button-blue']").click()

sleep(5)

# click on "Download: XLSX"

driver.find_element(By.LINK_TEXT, 'XLSX').click()
