'''
iFrame : an iframe is basically a webpage embedded inside another webpage.
        -> Selenium cannot directly interact with elements inside an iframe unless you first switch into it.

        -> in three ways we can switch in iframe
                1. using Index
                2. using web element
                3. using id or name
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get(r"D:\a_web_dev\practice_html\Selenium_iframe\page1.html")

driver.find_element(By.XPATH, '//input[@id="inp1"]').send_keys("First")

# driver.switch_to.frame(0)           # Using indexing
# driver.switch_to.frame("in2")       # Using name
# driver.switch_to.frame("frame2")      # Using id
driver.switch_to.frame( driver.find_element(By.XPATH, '//iframe[@id="frame2"]') )  # Using Web element

driver.find_element(By.XPATH, '//input[@id="inp2"]').send_keys("Second")

# driver.switch_to.frame(0)             # Using indexing
# driver.switch_to.frame("in3")         # Using name
# driver.switch_to.frame("frame3")         # Using id
driver.switch_to.frame( driver.find_element(By.XPATH, '//iframe[@id="frame3"]') )   # Using Web element

driver.find_element(By.XPATH, '//input[@id="inp3"]').send_keys("Third")


'''# Now to go back to parent element
driver.switch_to.parent_frame()
driver.find_element(By.XPATH, '//input[@id="inp2"]').send_keys("Rewriting in 2nd input")

driver.switch_to.parent_frame()
driver.find_element(By.XPATH, '//input[@id="inp1"]').send_keys("Rewriting in 1st input")'''

# Switch to default iframe
driver.switch_to.default_content()
driver.find_element(By.XPATH, '//input[@id="inp1"]').send_keys("Rewriting in 1st input")
