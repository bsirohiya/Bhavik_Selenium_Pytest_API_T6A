import os
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.amazon.in/")
driver.implicitly_wait(100)

driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("mobiles")
sleep(2)
driver.find_element(By.XPATH, '//div[@aria-rowindex="4"]').click()

driver.find_element(By.XPATH, '//span[@class="a-dropdown-label"]').click()
driver.find_element(By.XPATH, '//a[.="Newest Arrivals"]').click()

driver.find_element(By.XPATH, '//span[.="Free Shipping"]').click()

name = driver.find_element(By.XPATH, '(//div[@data-cy="title-recipe"])[1]').text
price = driver.find_element(By.XPATH, '(//span[@class="a-price-whole"])[1]').text

print(f"Name - {name}")
print(f"Price - {price}")