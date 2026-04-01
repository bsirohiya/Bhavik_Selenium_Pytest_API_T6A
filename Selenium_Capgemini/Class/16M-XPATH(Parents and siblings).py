'''
Traversing->

example ->
<div>
    <input>
    <input>
</div>

1. Forward ->       //div/input[1]
2. Backward ->      //input/..
'''

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless") # For not opening the browser, still giving value to terminal using print statement
driver = Chrome(options=o)
driver.maximize_window()

'''
Steps by using parent->
1. Identify static element
2. Move to common parent element for both static and dynamic element
3. Fetch dynamic element
'''

'''driver.get("https://demoqa.com/webtables")
salary = driver.find_element(By.XPATH, '//td[text()="Alden"]/../td[5]').text
print(f"Salary - {salary}")'''

'''driver.get("https://the-internet.herokuapp.com/tables")
dueAmt = driver.find_element(By.XPATH, '//td[text()="Frank"]/../td[4]').text
print(f"Due - {dueAmt}")'''


'''
Steps by using siblings->
    Types of siblings-
        1. Following siblings
        2. Preceding siblings
    
    Example-
        <tr>
            <td>U/A</td>           -> Dynamic element   -> Preceding sibling
            <td>Dhurandhar 2</td>  -> Static element    
            <td>*****</td>         -> Dynamic element   -> Following element
            <td>10 CR</td>         -> Dynamic element   -> Following element    
        </tr>    
        
        //td[text()="Dhurandhar 2"]//following-siblings::td[2] -> 10 CR
        //td[text()="Dhurandhar 2"]//preceding-siblings::td[1] -> U/A
'''

driver.get("https://the-internet.herokuapp.com/tables")
dueAmt = driver.find_element(By.XPATH, '//td[text()="Tim"]//following-sibling::td[2]').text
print(f"Due amount - {dueAmt}")

lastName = driver.find_element(By.XPATH, '//td[text()="Tim"]//preceding-sibling::td[1]').text
print(f"LastName - {lastName}")

