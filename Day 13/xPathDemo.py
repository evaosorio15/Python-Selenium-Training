from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver")
driver = webdriver.Chrome()

driver.maximize_window()


#absoulte xpath



#relative xpath