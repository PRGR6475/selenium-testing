from selenium import webdriver
"""
Xpath:
xpath are the xpath path expressions with helps to the xml objects.
This xpath is used to locate the element in the html
There are two types of xpaths:
1. Absolute xpath
2. Relative xpath
1.Absolute xpath:   
    It is more like the absolute path of any file 
    It start from the root of the element and end with the element
    It starts with the /

for example we have a parahraph tag in the html the absloute xpath for that element will be
/html/body/p[1]
for other paragraph tag it will be like 
/html/body/p[2]
for input tag it will 
/html/body/input[1]
    if we see it started from the root ie., html and ended at the tag
    It is not prefered as this not always reliable because some day a small change in the xpath 
    will make all other xpaths fail.


2. Relative Xpath:
    It is just like the relative path of any file
    It  starts with // (it means any where in the html) and followed by tagname , closed bracket inside 
    with prefix as @ to attributes , 
    if it is a function the approach will a little different
    for example:
        //input[@name="value"] 
        //*[@name="value"]
    * means any tag that has attribute name with value value.
    xpath provides options to use
OPTIONS:
<input id='inputId1' class='inputClass1' name='nameInput1' value="Hello world!"/>


and:
it is much more like the and statement in python 
returns the html element if the both the attributes or functions true
    
usage: //input[@name="value" and @id="value"]
ex - //input[@name="nameInput1" and @class="inputClass1"] this returns the element
    //h1[@class="h1Class" and text()="Second class"] this one attribute and function
    //h1[@class="h1Class" and contains(text(), 'S')] this one attribute and function and another function inside it

or :
it is also much like the or statemnet in python
returns the html element if the any one of the attribute or function true
usage: //input[@name='value' and @id='value']
ex - //input[@name="nameInput1" and @class="inputClass2"] this returns the element
    //h1[@class="h1Class3" and text()="Second class"] this one attribute and function we discuss about the text() function below
    //h1[@class="h1Class4" and contains(text(), 'S')] this one attribute and function and another function inside it 

FUNCTIONS:
<h1 id="h1Id" class="h1Class">Second class</h1>
There are many in xpath in them a few are disscussed 
these are important function

text():
    this doesnot take any arguments but we need to assign the text that exact text displayed on the page
usage:
//h1[text()="Second class"] this will return the h1 element for the page
This function can be used inside another function like contains, normalized-space also.



contains():
    This function take two mandiate arguments attribute or text function and its value and returns the elements that contains the 
    given attribute 

usage:
//h1[contains(@id, 'h1')] it will return two html elements
//h1[contains(text(),'Second class')] it will return two html h1 elements
//h1[contains(@class, 'h1')] it will return two html elements

the other functions will be discussed next day
"""

driver = webdriver.Chrome(executable_path="/Users/venkadesh/Desktop/chromedriver")
#try here to automate the facebook by tom.