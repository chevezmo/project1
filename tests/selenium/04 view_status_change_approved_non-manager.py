from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "./drivers/chromedriver.exe"
LINK = "http://127.0.0.1:5000/"
SLEEP_TIME = 2
USERNAME = "nbrinkler"
PASSWORD = "edRGd0Dy4PG"

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
history = driver.find_element_by_id("history")

history.click()
time.sleep(SLEEP_TIME)

# View Request

time.sleep(SLEEP_TIME)
history_back = driver.find_element_by_id("history_back")
history_back.click()

# Log out
time.sleep(SLEEP_TIME)
sign_out = driver.find_element_by_id("sign_out")
sign_out.click()
time.sleep(SLEEP_TIME)

driver.quit()