'''
Actionchains class

    Steps:
        1. Crearte object
        2. Store action
        3. Perform -> .perform()
'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

'''driver.get("https://demoqa.com/buttons")

driver.implicitly_wait(10)
actions = ActionChains(driver)

doubleClick = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
actions.double_click(doubleClick).perform()

rightClick = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
actions.context_click(rightClick).perform()

singleClick = driver.find_element(By.XPATH, '//button[.="Click Me"]')
actions.click(singleClick).perform()'''


'''# Scroll to the element function in action chain
driver.get("https://amazon.in/")

driver.implicitly_wait(100)
actions = ActionChains(driver)

bikeImg = driver.find_element(By.XPATH, '//img[@src="https://m.media-amazon.com/images/I/71eCO4ULXfL._AC_SY200_.jpg"]')
# actions.scroll_to_element(bikeImg).pause(2).click(bikeImg).perform()

actions.scroll_by_amount(0, 400).pause(2).scroll_by_amount(0, 400).pause(2).click(bikeImg).perform()

# input = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
# origin = ScrollOrigin.from_element(input)
# actions.pause(2).scroll_from_origin(origin, 0, 400).pause(2).click(bikeImg).perform()'''


'''# Mouse hover to element
driver.get("https://amazon.in/")

driver.implicitly_wait(100)
actions = ActionChains(driver)

signIn = driver.find_element(By.XPATH, '//div[@id="nav-link-accountList"]')
actions.pause(2).move_to_element(signIn).perform()'''


'''# Click and hold element
driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")

driver.implicitly_wait(100)
actions = ActionChains(driver)
sleep(2)
cross = driver.find_element(By.XPATH, '//span[@class="ng-tns-c2785778308-3 icon-cancel"]').click()
sleep(2)
input = driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("hehehe")
passEye = driver.find_element(By.XPATH, '//button[@tabindex="0"]')
actions.pause(2).click_and_hold(passEye).pause(2).release().perform()'''



# DRAG AND DROP
driver.get("https://demoqa.com/droppable")

draggable = driver.find_element(By.XPATH, '//div[@id="draggable"]')
droppable = driver.find_element(By.XPATH, '//div[@id="droppable"]')

actions = ActionChains(driver)
actions.pause(2).drag_and_drop(draggable, droppable).perform()
