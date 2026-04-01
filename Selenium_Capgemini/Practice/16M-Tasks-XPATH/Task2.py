from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://www.flipkart.com")
sleep(4)
driver.find_element(By.CLASS_NAME, "nw1UBF.v1zwn25").send_keys("Mobiles")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.find_element(By.XPATH, '//div[contains(@class, "RG5Slk")]/../..//div[@class="hZ3P6w DeU9vF"]').text)