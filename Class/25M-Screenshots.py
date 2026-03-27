import os
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://google.com")
driver.implicitly_wait(100)

# For taking screenshot of ENTIRE PAGE
# driver.save_screenshot("screenshot1.png")

# Another syntax
folder = os.path.join(os.getcwd(), "screenshots")   # To create folder
os.makedirs(folder, exist_ok=True)

driver.save_screenshot(f"{folder}/screenshot1.png")


# For taking Screenshot of a particular element
ele = driver.find_element(By.XPATH, '//div[@jscontroller="cnjECf"]')
ele.screenshot(f"{folder}/screenshot_ele.png")


# We can save screenshots name with time
ele2 = driver.find_element(By.XPATH, '//div[@class="vcVZ7d"]')
timestamps = time.strftime("%Y%m%d - %H%M%S")
ele2.screenshot(f"{folder}/screenshot_ele_{timestamps}.png")