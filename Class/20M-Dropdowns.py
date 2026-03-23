'''
Dropdowns are of 2 types
    1. Single
    2. Multiple


Types of Dropdown Implementation:
    1. Select ->
        Can be selected using 3 things
            1. visible text
            2. index
            3. value

    2. Custom
'''
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless") # For not opening the browser, still giving value to terminal using print statement
driver = Chrome(options=o)

# driver.get("file:///C:/Users/BHAVIK/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/LocalState/sessions/30A120DC7C45C8D124F92E04D2BB04A1B64263E0/transfers/2026-12/E22_Dropdowns.html")
# driver.maximize_window()


'''# SINGLE SELECT DROPDOWN
dropdown = driver.find_element(By.ID, "state")
option = Select(dropdown)

option.select_by_visible_text("Bihar")
sleep(2)
option.select_by_value("MH")
sleep(2)
option.select_by_index(0)'''


'''# MULTIPLE SELECT DROPDOWN

dropdown = driver.find_element(By.ID, "hobby")
option = Select(dropdown)

driver.find_element(By.XPATH, '//option[@value="dance"]').click()
driver.find_element(By.XPATH, '//option[@value="music"]').click()

# NOW WE CAN DESELECT BY SAME 3 OPTIONS
option.deselect_by_visible_text("Dance")
option.deselect_by_value("dance")
option.deselect_by_index(0)'''


driver.get("https://www.amazon.in")
driver.maximize_window()

driver.implicitly_wait(10)
sleep(4)

driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("mobiles")
searchingEles = driver.find_elements(By.XPATH, '//div[@class="s-suggestion-container"]')

for i in range(len(searchingEles)):
    print(searchingEles[i].text)

sleep(2)

searchingEles[3].click()