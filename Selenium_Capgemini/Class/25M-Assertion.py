'''
Using assert we are validating that outcome is same as expected outcome or not
When expected != actual then test case will fail
'''
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

'''driver.get("https://google.com")

# print(driver.title)

expected = "Google"
actual = driver.title
assert expected == actual, "Title mismatch"

driver.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys("hehehe")'''


# For amazon
driver.get("https://amazon.in/")
driver.implicitly_wait(100)
driver.find_element(By.XPATH, '//a[.="Bestsellers"]').click()

expected = "Amazon.in Bestsellers: The most popular items on Amazon"
actual = driver.title

assert expected == actual, "Title mismatch"
print("hehehe")

sleep(5)
driver.quit()