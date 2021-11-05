# selenium has many components to use but for web browser automation we use webdriver only so, we need to import the webdriver module from selenium library.
from selenium import webdriver
from datetime import time
driver = webdriver.Chrome(r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver")
driver.maximize_window()
#time.sleep(5)

driver.get("https://www.google.com")
driver.minimize_window()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

