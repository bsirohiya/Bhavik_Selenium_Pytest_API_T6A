'''
1. current_window_handle
2. window_handles
3. switch_to_window()
'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.google.com")

sleep(5)

# Manually open 3 tabs
print("Before")
print(driver.title)
print(driver.current_window_handle)

driver.switch_to.new_window()

driver.get("https://www.amazon.in/")

print("After")
print(driver.title)
print(driver.current_window_handle)

print(driver.window_handles)

driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.XPATH, '//a[.="About"]').click()