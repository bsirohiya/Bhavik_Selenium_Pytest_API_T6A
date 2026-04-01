from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

sleep(2)
actions = ActionChains(driver)

mouseHover = driver.find_element(By.XPATH, '//div[@class="dropdown"]')
actions.scroll_to_element(mouseHover).pause(2).move_to_element(mouseHover).perform()

sleep(2)

doubleClickCopy = driver.find_element(By.XPATH, '//button[.="Copy Text"]')
actions.double_click(doubleClickCopy).perform()

sleep(2)

draggable = driver.find_element(By.XPATH, '//div[@id="draggable"]')
droppable = driver.find_element(By.XPATH, '//div[@id="droppable"]')
actions.drag_and_drop(draggable, droppable).perform()