from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "./drivers/chromedriver.exe"
LINK = "http://127.0.0.1:5000/"
SLEEP_TIME = 2
USERNAME = "gbiernacki"
PASSWORD = "TfTm0yD7"
DESCRIPTION = "Plane Ticket - Toronto to New York - Round Trip"
AMOUNT = "547.36"
EXPENSE_TYPE = "travel"


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

# Submit Request
description = driver.find_element_by_id("description")
amount = driver.find_element_by_id("amount")
expense_type = driver.find_element_by_id(EXPENSE_TYPE)
submit_request = driver.find_element_by_id("submit_request")

description.send_keys(DESCRIPTION)
amount.send_keys(AMOUNT)
expense_type.click()
time.sleep(SLEEP_TIME)

submit_request.click()
time.sleep(SLEEP_TIME)

# View Request
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