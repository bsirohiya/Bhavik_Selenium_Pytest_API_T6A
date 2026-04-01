from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

'''# ENTER KEY
driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)
input = driver.find_element(By.XPATH, '//input[@id = "twotabsearchtextbox"]')
input.send_keys("mobiles")
input.send_keys(Keys.ENTER)'''


# COPY AND PASTING
driver.get("https://demoqa.com/text-box")
driver.implicitly_wait(5)
currAddress = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
currAddress.send_keys("hehehe")
currAddress.send_keys(Keys.CONTROL + "a")
currAddress.send_keys(Keys.CONTROL + "c")

permaAddress = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
permaAddress.send_keys(Keys.CONTROL + "v")