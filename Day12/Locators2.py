#Introduction to various locators for identifying web elements.
#Built-in locators like ClassName and TagName


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


##Chrome path
serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
##chrome through variable environment
#driver = webdriver.Chrome()

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

##this will return multiple SLIDERS
sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
##this will print the amount of sliders
print(len(sliders))  ## 5 total numbers of sliders

##this will return ALL ('a') the LINKS
links=driver.find_elements(By.TAG_NAME,'a')
##this will print the amount of sliders
print(len(links))  ## 88 total number of links

