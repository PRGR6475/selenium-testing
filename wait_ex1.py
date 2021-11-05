
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/venkadesh/Desktop/chromedriver")
driver.get('file:/Users/venkadesh/Desktop/untitled folder/selenium_class/waits2.html')



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


"""
Here i have used visibility_of_element_located class
This returns True if the element is visible in dom and also in page.
use the waits2.html for this 
"""
driver.find_element_by_id('btn').click()
print(WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, 'para'))).text)
