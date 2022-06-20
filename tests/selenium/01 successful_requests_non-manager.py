from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "./drivers/chromedriver.exe"
LINK = "http://127.0.0.1:5000/"
SLEEP_TIME = 2
USERNAME = "rbritt"
PASSWORD = "Lb7uK5HKRl"
DESCRIPTION1 = "Office Supplies"
AMOUNT1 = "21.25"
EXPENSE_TYPE1 = "supplies"
DESCRIPTION2 = "Excel Training"
AMOUNT2 = "199.88"
EXPENSE_TYPE2 = "education"

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
request = driver.find_element_by_id("request")

request.click()
time.sleep(SLEEP_TIME)

# Submit 1st Request
description = driver.find_element_by_id("description")
amount = driver.find_element_by_id("amount")
expense_type = driver.find_element_by_id(EXPENSE_TYPE1)
submit_request = driver.find_element_by_id("submit_request")

description.send_keys(DESCRIPTION1)
amount.send_keys(AMOUNT1)
expense_type.click()
time.sleep(SLEEP_TIME)

submit_request.click()
time.sleep(SLEEP_TIME)

# Submit 2nd Request
description = driver.find_element_by_id("description")
amount = driver.find_element_by_id("amount")
expense_type = driver.find_element_by_id(EXPENSE_TYPE2)
submit_request = driver.find_element_by_id("submit_request")

description.send_keys(DESCRIPTION2)
amount.send_keys(AMOUNT2)
expense_type.click()
time.sleep(SLEEP_TIME)

submit_request.click()
time.sleep(SLEEP_TIME)

# View Requests
request_back = driver.find_element_by_id("request_back")
request_back.click()

history = driver.find_element_by_id("history")
time.sleep(SLEEP_TIME)
history.click()

time.sleep(SLEEP_TIME)
history_back = driver.find_element_by_id("history_back")
history_back.click()

# Log out
time.sleep(SLEEP_TIME)
sign_out = driver.find_element_by_id("sign_out")
sign_out.click()
time.sleep(SLEEP_TIME)

driver.quit()