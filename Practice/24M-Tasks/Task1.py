from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://x.com/?lang=en")
driver.implicitly_wait(100)

driver.switch_to.frame( driver.find_element(By.XPATH, '//iframe[@title="Sign in with Google Button"]') )

driver.find_element(By.XPATH, '//div[@id="container-div"]').click()

sleep(5)
driver.quit()