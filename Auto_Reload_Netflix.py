# Autor: MOHAMAD SAIFUL AFFENDY
# DATE: 06082019:0023

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By as b
import time

# Open Chrome with Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.smartdnsproxy.com/Login/")

# Input E-mail addresss and password
driver.find_element_by_id("txtEmail").send_keys("<EMAIL ADDRESS>")
driver.find_element_by_id ("txtPassword").send_keys("<PASSWORD>")

# Click Submit button
driver.find_element_by_id("btnSignIn").click()

# Update current IP Address in Smart DNS Proxy system
# Auto click JavaScript element every 3 minute 
c=500
while c > 0:
	print("Updating IP Address ")
	time.sleep(10)
	javasc = driver.find_element_by_id("lnkUpdateMyIP")
	driver.execute_script("arguments[0].click();", javasc)
	c-=1
	print("Sleeping 3 minutes")
  time.sleep(180)
	
