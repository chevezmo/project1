from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "./drivers/chromedriver.exe"
LINK = "http://127.0.0.1:5000/"
SLEEP_TIME = 2
USERNAME = "gbiernacki"
PASSWORD = "TfTm0yD7"

driver = webdriver.Chrome(PATH)
driver.get(LINK)

# Login
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
submit = driver.find_element_by_id("submit_login")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)

submit.click()
time.sleep(SLEEP_TIME)

# Account Menu
request = driver.find_element_by_id("approval")

request.click()
time.sleep(SLEEP_TIME)

# Approve Request
approve = driver.find_element_by_id('approve1')

approve.click()
time.sleep(SLEEP_TIME)

# Reject Request
reject = driver.find_element_by_id('reject2')

reject.click()
time.sleep(SLEEP_TIME)

# Log out
approval_back = driver.find_element_by_id('approval_back')
approval_back.click()

time.sleep(SLEEP_TIME)
sign_out = driver.find_element_by_id("sign_out")
sign_out.click()
time.sleep(SLEEP_TIME)

driver.quit()