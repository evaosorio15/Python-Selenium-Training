from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.bankrate.com")
driver.maximize_window()


## ABSOLUTE XPath
#driver.find_element(By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/button[1]").click()

#driver.find_element(By.XPATH, "/html[1]/body[1]/header[1]/div[3]/form[1]/input[1]").send_keys("Balance transfer credit cards")

#driver.find_element(By.XPATH, "/html[1]/body[1]/header[1]/div[3]/form[1]/button[1]/div[1]").click()


## RELATIVE XPath
#driver.find_element(By.XPATH, "//button[@aria-label='Open search modal or press the home key to return to the main menu']").click()

#driver.find_element(By.XPATH, "//input[@id='siteSearchInput']").send_keys("Car insurance quotes")

#driver.find_element(By.XPATH, "//div[@x-show='!isSubmitting']").click()



#driver.find_element(By.XPATH, "//div[@x-show='!isSubmitting']").click()


## contains()
#driver.find_element(By.XPATH, "//button[contains(@x-ref,'siteNavSearch')]").click()
## starts-with()
#driver.find_element(By.XPATH, "//input[starts-with(@id,'siteSearch')]").send_keys("Car insurance quotes")

#driver.find_element(By.XPATH, "//div[@x-show='!isSubmitting']").click()

# text()
driver.find_element(By.XPATH, "//span[text()='High-yield savings']").click()