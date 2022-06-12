from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "drivers/chromedriver.exe"

chrome_driver = webdriver.Chrome(path)
chrome_driver.get("https://images.google.ca")
search_box = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys("Cats")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
chrome_driver.quit()