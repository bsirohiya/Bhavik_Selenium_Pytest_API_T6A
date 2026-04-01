from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()
print(driver.find_element(By.XPATH, '//h2[contains(@aria-label, "iQOO ")]/../../..//span[@class="a-price-whole"]').text)