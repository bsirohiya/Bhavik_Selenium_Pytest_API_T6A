import os
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(100)

driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("locked_out_user")
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauc")
driver.find_element(By.XPATH, '//input[@id="login-button"]').click()

expected = "https://www.saucedemo.com/inventory.html"
actual = driver.current_url

try:
    assert expected == actual
except:
    driver.save_screenshot("screenshot1.png")

time.sleep(5)
driver.quit()