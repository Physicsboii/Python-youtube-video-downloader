from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys







link = "Give the video link here"


driver = webdriver.Safari()
driver.get("https://www.savefrom.net")
share = driver.find_element_by_id("sf_url")
share.click()
time.sleep(2)
share.send_keys(link)
time.sleep(2)
share.send_keys(Keys.RETURN)

time.sleep(5)

down = driver.find_element_by_class_name("def-btn-box")
down.click()

time.sleep(5)
driver.quit()
