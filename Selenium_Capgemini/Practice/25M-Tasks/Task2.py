from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://in.pinterest.com/")
driver.implicitly_wait(100)

driver.save_screenshot("pageScreenshot.png")

picture = driver.find_element(By.XPATH, '//img[@src="https://s.pinimg.com/webapp/visual-search-1px-ecc706bc.png"]')
picture.screenshot("picScreenshot.png")

sleep(5)
driver.quit()
