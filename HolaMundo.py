from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Corrige el path como raw string o escapado
# service = Service(r"C:\SeleniumDrivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
#
# driver.get("http://demoqa.com/text-box")
#
# print(driver.title)
#
# print("*************************************")
#
# driver.close()
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/text-box")
# driver.implicitly_wait(0.5)