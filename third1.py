"""
alerts or browser pops are of three types
1. alerts with message and ok/accept button
2. alerts with message, ok/accept and dismiss/cancel button
3. alerts with message, ok/accept, dismiss/cancel and input box 
 we can handle alerts with selenium using switch_to function and alert from driver class.
"""
import time
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver"
)
driver.get(r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver")
time.sleep(3)
#find_element_by_tag_name("button") will give the button element over which cilck() 
#function will do the cilck operation.
driver.find_element_by_tag_name('button').click()
time.sleep(3)
#driver.switch_to.alert the alert object by which we get text, or we can accept / dismiss alert.
#In the below step i have assigned/ store the reference of alert obj in alert_obj
#returned by driver.switch_to.alert
alert_obj = driver.switch_to.alert

#.text with return the text of any element here it will return the text of alert.
print(alert_obj.text)
time.sleep(5)
#.accept() will not take any agruments but accepts the alert/ click ok button
alert_obj.accept()