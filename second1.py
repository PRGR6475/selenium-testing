from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver")

driver.maximize_window()

#Replace the file path with html 
#for windows it will be like file://C:/Desktop/first.html

driver.get('file:/Users/R G REDDY PEDDIREDDY/Desktop/html & css/selenium_scripts/html/first.html')

#current_url function will not take any arguments and return the current url of the tab
print(driver.current_url)

"""
Locators:
--Locators will helps selenium webdriver find the html element to perform the action
They are Two types of locators
1. Normal Locators
2. Customized Locators

1.Normal Locators
 a. id:
    <h1 id="h1Id" class="h1Class">Second class</h1>
    The above is the h1 heading html tag for which there is attribute id with value "h1Id" by using this 
    we can locate this element.
    selenium provide the api or method find_element_by_id()
    find_element_by_id() takes one argumnet value of id of that element as mandiate argument
    and this returns the html element if Found else NoSuchElementException.
    *value of id should be provided as string.

b. name:
    <input id='inputId1' class='inputClass1' name='nameInput1' value="Hello world!"/>
    The above is Input thtml tag with having the "name" attribute with value "nameInput1" by using this we can 
    locate this element.
    selenium provide the api or method find_element_by_name()
    find_element_by_name() takes one argument value of name of that element as mandiate argument and
    this returns the html element if found else NoSuchElementException.
    *value of name should be provided as string.
c. class name:
     <p id='pId' class="pClass">This is second class of selenium and today we see how to get the data from tags,
         and window handling</p><br/>
    The above is paragraph tag  which  having the "class" attribute with value "pClass" by using this we can locate 
    this element.
    selenium provide the method find_element_by_class_name()
    find_element_by_class_name() takes one argumnet value of class pf that element as mandiate argument and
    this returns the html element if found else NoSuchElementException.
    *value of name should be provided as string.

d. tag_name:
    <a href="https://www.gmail.com/" target="_blank">Gmail.com</a><br/>
    The above is anchor tag which having the tag name "a" by using this we can locate this element.
    selenium provide the method find_element_by_tag_name()
    find_element_by_tag_name() takes one argumnet tag name as mandiate argument and returns the html element if found else
    NoSuchElementException.
    *Tag name should be provided as string.

e.link_text and partial_link_text:
    <a href="https://www.gmail.com/" target="_blank">Gmail.com</a><br/>
    The above link text or anchor tag has the text "Gmail.com" we can locate this element.
    selenium provide method find_element_by_link_text() and find_element_by_partial_link_text()
    both the method takes one mandiate arguments link_text() takes the exact text of that tag as argument 
    and partial_link_text() takes the any part of the text of that tag as argument.
    Both will return the html element if found else NoSuchEelementException.
    *text for link_text and partial_limk_text should be provide as string.

"""
anchor_tag = driver.find_element_by_tag_name('h1')
print(anchor_tag.text)
id = driver.find_element_by_id('pId')
print(id.text)
print(id.get_attribute('id'))
name = driver.find_element_by_name('nameInput2')
print(name.get_attribute('placeholder'))
print(driver.find_element_by_link_text('Gmail.com').text)
print(driver.find_element_by_partial_link_text('Google').text)
print(driver.find_element_by_class_name('hClass').text)

#The above all find_elemnt_by functions contains other function like text, get_attribute, 
#click() if it is clickable, send_keys() if it is input field , location etc, will be disscussed on later classes

# .text will return the actual text that is displaed in html
id = driver.find_element_by_id('pId')
print(id.text)
#.get_attribute() will take one mandiate argument attribute of that element as string 
#and return the value of that html element.
print(id.get_attribute('id'))
name = driver.find_element_by_name('nameInput2')
print(name.get_attribute('placeholder'))



# driver.get('https://www.google.com/')
# http://127.0.0.1:5500/selenium_scripts/html/first.html
# curr = driver.current_window_handle
# print('the current window obj is', curr)
# time.sleep(5)
# driver.find_element_by_tag_name('a').click()
# print(driver.window_handles)
# time.sleep(5)
# driver.switch_to_window(curr)
# time.sleep(5)
# driver.find_element_by_tag_name('a').click()
# print(driver.window_handles)

# print(dir(driver.find_element_by_tag_name('a')))
# driver.set_window_position(0,300)
# driver.set_window_size(0,200)

# driver.fullscreen_window()
# time.sleep(5)
# a = driver.get_window_position()
# print('browser position', a)
# b = driver.get_window_rect()
# print('browser, window postion', b)
# c = driver.get_window_size()
# print('browser size',c)