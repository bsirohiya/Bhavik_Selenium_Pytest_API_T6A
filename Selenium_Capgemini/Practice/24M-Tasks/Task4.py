from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, '//button[.="Click for JS Alert"]').click()
print(driver.switch_to.alert.text)
sleep(2)
driver.switch_to.alert.accept()
sleep(2)

driver.find_element(By.XPATH, '//button[.="Click for JS Confirm"]').click()
print(driver.switch_to.alert.text)
sleep(2)
driver.switch_to.alert.accept()
sleep(2)

driver.find_element(By.XPATH, '//button[.="Click for JS Prompt"]').click()
promptAlert = driver.switch_to.alert
print(promptAlert.text)
promptAlert.send_keys("hehehe")
sleep(2)
driver.switch_to.alert.accept()


sleep(5)
driver.quit()