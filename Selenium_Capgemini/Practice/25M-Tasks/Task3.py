from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.lenskart.com/")
driver.implicitly_wait(100)

driver.find_element(By.XPATH, '//a[.="EYEGLASSES"]').click()

expected = "https://www.lenskart.com/eyeglasses.html"
actual = driver.current_url

assert expected == actual, "Error"

# Use because actual screen is not visible because mouse is hovering at EYEGLASSES even after clicking it
toRemoveMousePtr = driver.find_element(By.XPATH, '//a[.="Corporate"]')
actions = ActionChains(driver)
actions.move_to_element(toRemoveMousePtr).perform()

dropdown = driver.find_element(By.XPATH, '//select[@id="sortByDropdown"]')
option = Select(dropdown)

option.select_by_value("popular")

driver.save_screenshot("screenshot.png")

sleep(5)
driver.quit()