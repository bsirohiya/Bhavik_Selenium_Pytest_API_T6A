from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.implicitly_wait(100)
actions = ActionChains(driver)

'''simple_alert = driver.find_element(By.XPATH, '//button[@id="alertBtn"]')
actions.scroll_to_element(simple_alert).pause(2).click(simple_alert).perform()
sleep(2)
driver.switch_to.alert.accept()'''

'''confirmation_alert = driver.find_element(By.XPATH, '//button[@id="confirmBtn"]')
actions.scroll_to_element(confirmation_alert).pause(2).click(confirmation_alert).perform()
sleep(2)
driver.switch_to.alert.accept()'''

prompt_alert = driver.find_element(By.XPATH, '//button[@id="promptBtn"]')
actions.scroll_to_element(prompt_alert).pause(2).click(prompt_alert).perform()
sleep(2)
alert = driver.switch_to.alert
alert.send_keys("hehehe")
sleep(2)
alert.accept()

