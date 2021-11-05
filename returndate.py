import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\R G REDDY PEDDIREDDY\Desktop\chromedriver")
driver.get("https://www.redbus.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//label[text()="Return date"]').click()


# month_year = driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
# print(month_year)

# you can uncomment and comment other lines in the below function for dynamic thing and call the function with argumnets
def select_date():
    # def select_date(day, month_and_year):
    month_year = driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="monthTitle"]').text
    if month_year == 'Jan 2022':
        # if month_year == str(month_and_year):
        driver.find_element_by_xpath("""//div[@class="rb-calendar"]//td[text()='3']""").click()

        # driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[text()='+'{}'.format(str(day))+']').click()
    else:
        time.sleep(3)
        driver.find_element_by_xpath('//div[@class="rb-calendar"]//td[@class="next"]').click()
        select_date()
        # select_date(day, month_and_year)


select_date()
# select_date(4, 'Jan 2022')
# please try the same aproach in redbus to Return Date by Tuesday
# And also the facebook create page also.
# Try the webdriver manager also

"""
The xpaths remaining functions 
starts-with():
    This function will take two mandiate argumnets attribute and its value as string and return the html elements 
    that starts with the value.
#The example are refering to the first.html
//h1[starts-with(@class, 'h1')] This will return two html tags
not():
    This function will take two mandiate arguments attribute and its value and return the matching html element 
    which doesnot have that attributes
//h1[starts-with9@class, 'h1) and not(@class='h12Class')] this will return the one h1 element

position():
    This function doesnot take any argumnets, but we need to assign a value to the function, it more like 
    the indexing and return that index html element

//h1[starts-with(@class, 'h1')] this will return two html tags in that to select the second one we use
//h1[starts-with(@class, 'h1)][1] or (//h1[starts-with(@class, 'h1)])[1]
with position() function (//h1[starts-with(@class, 'h1')])[position()=1] or //h1[starts-with(@class, 'h1)][position()=1]

last():
    This function is similar to position(), The only diff is no need to assign the value for this and it will return the 
    last one in the index
//h1[starts-with(@class, 'h1')][last()] 
we can also substarct this function so that we get result index one tag
ex - the above example last() =  2 index
last()-1 = 1 index
//h1[starts-with(@class, 'h1')][last()-1] this one will return the first one

"""
# This refers to the axes.html
"""
Xpath axes:
 child:
    //div[@id='Y2']/child::* this will return all the childs of Y2
    //div[@id='Y2']/child::div[@id='M2']/child::* this will return the childs of M2
 parent:
    //div[@id='Y2']/parent::* this will return the parents of Y2 (B2)
    //div[@id='Y2']/parent::div this will return the parent div tag of Y2 (B2)
    //div[@id='Y2']/parent::div/parent::* this will return the parent tags of B2 (A)
 ancestor:
    //div[@id='Y2']/ancestor::*
 following-sibling:
    //div[@id='Y2']/following-sibling::*
 preceding-sibling:
    //div[@id='Y2']/preceding-sibling::*

"""