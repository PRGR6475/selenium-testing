import time
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver")
driver.get(r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver")
time.sleep(3)

driver.find_element_by_tag_name('button').click()
time.sleep(3)
alert_obj = driver.switch_to.alert
print(alert_obj.text)
time.sleep(5)
alert_obj.accept()
alert_obj.dismiss()
