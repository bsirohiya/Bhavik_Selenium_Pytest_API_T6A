from time import sleep
from selenium.webdriver import Chrome, ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://facebook.com")
print(f"1st tab -> Title : {driver.title} AND URL : {driver.current_url}")

driver.switch_to.new_window()

driver.get("https://google.com")
print(f"2nd tab Title : {driver.title} AND URL : {driver.current_url}")

driver.switch_to.new_window()

driver.get("https://bcci.tv")
print(f"3rd tab Title : {driver.title} AND URL : {driver.current_url}")

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()

sleep(5)
driver.quit()