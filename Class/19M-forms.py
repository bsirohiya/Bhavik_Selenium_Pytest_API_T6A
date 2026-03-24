from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless") # For not opening the browser, still giving value to terminal using print statement
driver = Chrome(options=o)
driver.maximize_window()

'''driver.get("https://demoqa.com/automation-practice-form")

driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys("Ram")
driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys("Krishn")
driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys("krishn@gmail.com")
driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys("741852963")
driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
driver.find_element(By.XPATH, '//div[@aria-label="Choose Saturday, March 21st, 2026"]').click()
driver.find_element(By.XPATH, '//input[@value="Male"]').click()
driver.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys("741852963 hehehehehe")
driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-1"]').click()
driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-3"]').click()
driver.find_element(By.XPATH, '//input[@id="uploadPicture"]').send_keys(r"D:\Extra work\CORE Subjects.docx")
driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys("helloooooooooooo")'''


'''
# For selecting date
driver.get("https://www.irctc.co.in/nget/train-search")
selectDate = driver.find_element(By.XPATH, '//input[@class="ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]')
selectDate.click()
forwardBtn = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9"]')
forwardBtn.click()

date = driver.find_element(By.XPATH, '(//a[@class="ui-state-default ng-tns-c69-9 ng-star-inserted"])[1]')
date.click()
'''


driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()

driver.find_element(By.XPATH, '//select[@class="react-datepicker__month-select"]').click()
driver.find_element(By.XPATH, '//option[.="May"]').click()

driver.find_element(By.XPATH, '//select[@class="react-datepicker__year-select"]').click()
driver.find_element(By.XPATH, '//option[.="2004"]').click()

driver.find_element(By.XPATH, '//div[.="15"]').click()
