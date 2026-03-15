##Customized Locators (CSS Selectors)
##1. Tag & Id  (tagname#valueId = input#email)
##2. Tag & Class
##3. Tag & Attribute
##4. Tag & Class Attribute

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


##Chrome path
serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
##chrome through variable environment
#driver = webdriver.Chrome()

driver.get("http://www.facebook.com")
driver.maximize_window()

##1. Tag & Id - email
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

##2. Tag & Class - inputtext _55r1 _6luy
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

##3. Tag & attribute - data-testid="royal-email
#driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal-email]").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR, "[data-testid=royal-email]").send_keys("abc@gmail.com")

##4, Tag & Class & Attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal-pass]").send_keys("xyz")