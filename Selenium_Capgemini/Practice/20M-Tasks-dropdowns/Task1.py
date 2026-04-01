from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.zomato.com/jaipur/restaurants")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//input[@class="sc-dBfaGr dyyfrm"]').send_keys("Rice")
driver.find_element(By.XPATH, '//input[@class="sc-dBfaGr dyyfrm"]').click()

products = driver.find_elements(By.XPATH, '//div[@class="sc-glUWqk GrjUP"]')

for i in products:
    print(i.text)

products[1].click()