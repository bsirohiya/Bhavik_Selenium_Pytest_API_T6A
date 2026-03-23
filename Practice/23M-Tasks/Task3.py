from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.flipkart.com")
driver.implicitly_wait(10)

# Going to the bottom/footer of the page
driver.find_element(By.XPATH, '//span[@class="b3wTlE"]').click()
actions = ActionChains(driver)

footer = driver.find_element(By.XPATH, '//div[@class="EGBsCF"]')
actions.scroll_to_element(footer).perform()
sleep(2)

# Going to MYNTRA
myntra = driver.find_element(By.XPATH, '//a[.="Myntra"]')
actions.click(myntra).perform()

sleep(2)
driver.switch_to.window(driver.window_handles[1])
print("For MYNTRA 2nd Tab : ")
print(f" id = {driver.current_window_handle}")
print(f" title = {driver.title}")
print(f" url = {driver.current_url}")
print()

sleep(3)
driver.switch_to.window(driver.window_handles[0])
actions.scroll_to_element(footer).perform()
sleep(2)

# Going to CLEARTRIP
clearTrip = driver.find_element(By.XPATH, '//a[.="Cleartrip"]')
actions.click(clearTrip).perform()

sleep(2)
driver.switch_to.window(driver.window_handles[2])
print("For CLEARTRIP 3rd Tab : ")
print(f" id = {driver.current_window_handle}")
print(f" title = {driver.title}")
print(f" url = {driver.current_url}")
print()

sleep(3)
driver.switch_to.window(driver.window_handles[0])
actions.scroll_to_element(footer).perform()
sleep(2)

# Going to SHOPSY+
shopsy = driver.find_element(By.XPATH, '//a[.="Shopsy"]')
actions.click(shopsy).perform()

sleep(2)
driver.switch_to.window(driver.window_handles[3])
print("For SHOPSY 4th Tab : ")
print(f" id = {driver.current_window_handle}")
print(f" title = {driver.title}")
print(f" url = {driver.current_url}")
print()
