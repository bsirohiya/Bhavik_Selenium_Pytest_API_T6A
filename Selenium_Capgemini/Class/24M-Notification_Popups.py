from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_experimental_option('prefs', {"safebrowsing.enabled": True})
# o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.maximize_window()

'''driver.get("https://www.python.org/downloads/")
driver.implicitly_wait(100)
driver.find_element(By.XPATH, '(//a[.="Python 3.14.3"])[4]').click()'''


driver.get("https://www.easemytrip.com/")