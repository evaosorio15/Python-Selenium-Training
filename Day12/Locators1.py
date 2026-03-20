#Introduction to various locators for identifying web elements.
#Built-in locators like ID, Name, LinkText, PartialLinkText and explores customized options such as CSS selectors.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


##Chrome path
serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
##chrome through variable environment
#driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


##id
#driver.find_element(By.ID,"small-searchterms").send_keys("Leica T Mirrorless Digital Camera")
##name locators
driver.find_element(By.NAME,"q").send_keys("Leica T Mirrorless Digital Camera")


##testing full link text name
#driver.find_element(By.LINK_TEXT,"Register").click()
##testing only partial the link text name
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
