from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/venkadesh/Desktop/chromedriver")
driver.get('file:/Users/venkadesh/Desktop/untitled folder/selenium_class/waits.html')


"""
In the modren web pages the DOM (Documnet Object Model) objects will take will to load
sometimes it depends on the network  speed and webapplication speed etc, 
But selenium script doesnot know when to wait and where,
We can stop the flow of the script by using sleep function from time module,
Though it works, we should not use this function more often.
Because the sleep() will wait for specified time in seconds even if element appears
earlier that. This is not a good practise.

Selenium provides waits concept to counter that type of problems
The waits in selenium are classsified into three
1. Implicitly_wait:
    This type of wait is like global one, It means you need to specify only one time
    and it will consider for enitre session (untill we use driver.quit()).

    This is a method/function of webdriver class which takes one mandiate argument
    time in seconds as int. and it will for wait for DOM element for that specified time.
    if that element found with in the specified time, it will get that element as soon as 
    the element found, else it will throw  the exception (if the element not appear in the 
    specified time)
    
Note:
dirver.close() do close the window that is in focus only but not all.
where as driver.quite() will close the enitre tabs and session also.

USAGE:
"""
driver.implicitly_wait(15)
driver.find_element_by_id('btn').click()
print(driver.find_element_by_id('h1').text)
"""
In the example html thier is button with id "btn" which will turns into red color on click 
after some time in a h1 tag with id 'h1' will be visible, to grab the text from that message 
we should wait, In above i was using the implicit wait concept 
i have give 15sec to the implicitly_wait() function so it will wait for 15sec and at 16second 
it will rasise the exception. if it found with in that 15sec it will get that element
"""
"""
2. Explicit wait:
    This one is a little different from implicit one, it wait for the specifed time based on the 
    condition
    WebDriverWait is class from wait module.
    we can import this from webdriver.support.ui 
    This class takes four argumnets two mandiate and two options.
    The two mandite arguments are
    a. webdriver object (driver)
    b. timeout (time in sec ie., maximum time to wait)
    We will discuss the other two optional waits in Flutent wait concept
    and it has two methods/functions to use based on condition
    a. untill 
        This function take the three argumnets one mandiate other optional.
        mandiate one is the object  of class from  excepted_condition module 
        and wait for that condition to satisfy
        The excepted_condition are the class support.expected_condition.py module  
        It is more like 
        untill(True/False)
    
    b. untill_not 
        This will works in oppsite to the untill function. the arguments will same as that function.
In the below two lines of code i have used one class presence_of_element_located() from 
expected_conditions module.
it will take the locator as tuple containing   By class variable.
presence_of_element_located() it will check for the element is present in the dom or not 
it does't need to be visible in the page and return True/False 
By is class from by module it has few class varibles by which we use the locators
like 
By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.CSS_SELECTOR
By.PARTIAL_LINK_TEXT
By.LINK_TEXT
By.XPATH

"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By

driver.find_element_by_id('btn').click()
element = WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, 'h1')))
print(element.text)

#in the above line of code i have written that more detail
#Below this how it is used in real time
from selenium.webdriver.support import expected_conditions as EC

print(WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'h1'))).text)

#Note: Please do comment the implicit wait code lines to runs the above.

"""
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

These are the other classes in expected_conditions module by seeing the names of 
the class iteself we can understand what the function will do
Read the function and ask me if you have any doubts.
"""