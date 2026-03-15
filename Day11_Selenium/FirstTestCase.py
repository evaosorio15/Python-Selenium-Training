#Test Case 1
#1.	Open web browser (Chrome/IE…etc.)
#2.	Open URL  https://opensource-demo.orangehrmlive.com/
#3.	Provide email:  Admin
#4.	Password: Admin123
#5.	Click login
#6.	Capture title of the home page
#7.	Verify title of the page: “OrangeHRM”
#8.	Close browser

#Below is the old way of scripting to Selenium versions prior to 4.10+
#from selenium import webdriver
#driver=webdriver.Chrome("C:\Drivers\chromedriver-win64\chromedriver.exe")
#driver.get("https://opensource-demo.orangehrmlive.com/")

##New scripting for Selenium 4.10+
##1-8
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
##addition needed to use WebDriverWait to wait until the element is present
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

##Chrome
##serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
##driver = webdriver.Chrome(service=serv_obj)
#driver = webdriver.Chrome()

##Edge
##serv_obj = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
##driver = webdriver.Edge(service=serv_obj)
#driver = webdriver.Edge()

#driver.get("https://opensource-demo.orangehrmlive.com/")

##waiting 10 seconds
#wait = WebDriverWait(driver, 10)

## WAIT for the username field
#username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#username.send_keys("Admin")

#password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
#password.send_keys("admin123")

#login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#login_btn.click()

##Validate login using page title
#if driver.title == "OrangeHRM":
 #   print("Login Test Passed")
#else:
 #   print("Login Test Failed")

#driver.close()



#Test Case 2
#1.	Open web browser (Chrome/IE…etc)
#2.	Open URL https://admin-demo.nopcommerce.com/login
    #Need to first clear the text box: “driver.find_element(by.Name,”Email”).clear()
#3.	Provide email: admin@yourstore.com
    #Need to first clear the text box: “driver.find_element(by.Name,”Password”).clear()
#4.	Password: admin
#5.	Click login
    #driver.find_element(By.XPATH,”//*[@id="main"]/div/section/div/div[2]/div[1]/div/form/div[3]/button”).click()
#6.	Capture title of the dashboard page (actual title)
#7.	Verify title of the page: “Dashboard / nopCommerce administration”
#8.	Close browser

#New scripting for Selenium 4.10+
#1-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#addition needed to use WebDriverWait to wait until the element is present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##Chrome
#serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service=serv_obj)
#driver = webdriver.Chrome()

##Edge
serv_obj = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
#driver = webdriver.Edge()

driver.get("https://admin-demo.nopcommerce.com/login")

#waiting 10 seconds
wait = WebDriverWait(driver, 15)


# WAIT for the username field
Email = wait.until(EC.presence_of_element_located((By.NAME, "Email")))
Email.clear()
Email.send_keys("admin@yourstore.com")

Password = wait.until(EC.presence_of_element_located((By.NAME, "Password")))
Password.clear()
Password.send_keys("admin")

#login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#login_btn.click()

driver.find_element(By.XPATH,"/html/body/div[6]/main/div/section/div/div[2]/div[1]/div/form/div[3]/button").click()

#NOW WAIT FOR DASHBOARD
#wait.until(EC.title_contains("Dashboard"))

#Validate login using page title
#print("Actual title Selenium sees:", driver.title)
if driver.title == "Dashboard / nopCommerce administration":
#if "Dashboard" in driver.title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()

