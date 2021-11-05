import time
from selenium import webdriver
"""
Customized locators
For locating the element/elements there are two types of 
customized locators
1. css selector
2. xpath
1. css selector:
By using css attributes we can locate element/elements
css attribute like id, class, other attributes
selenium prodives the function/api find_element_by_css_selector()
It will take the css selector argumnet as string and locate the element.
css selector usage:
id:
    for using the id attribute we should use the symbol # infront of the value
ex- find_element_by_css_selector('#id')
class:
    for using the class attribute we should use the symbol . infront of the value
ex - find_element_by_css_selector('.class')

for using the other attributes like name or any
tagname[attributename]
find_element_by_css_selector('tagename[attributename]')
ex - find_element_by_css_selector('input[name]')
"""

driver = webdriver.Chrome(executable_path=r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver")

driver.get('https://www.google.com/')
# ../html/first.html
driver.maximize_window()
# h1_text = driver.find_element_by_css_selector('#h1Id')
# print(driver.find_element_by_css_selector('.h1Class').text)
# # print(h1_text.text)
# # print(driver.find_element_by_css_selector('p[name]').text)
# print(driver.find_element_by_css_selector('p.pClass[name]').text)
time.sleep(4)
driver.find_element_by_name('q').send_keys('india')
time.sleep(3)
"""
find_elements_by_xpath
find_elements_by_id
find_elements_by_class_name
find_elements_by_css_selector
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
The above all the functions/apis provided by the selenium will return the list of hmtl element objects if the 
locators are provided.
example was is discussed in below 
"""
suggestions_list = driver.find_elements_by_xpath('//li[@data-view-type="1"]')
for suggestion  in suggestions_list:
    print(suggestion.text)

