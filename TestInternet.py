import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 1. Create an object from Options class
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Tip

# 2. Driver init
driver = webdriver.Chrome(options=chrome_options)

# 3. Start the automated flow
driver.implicitly_wait(10)
driver.get("https://www.speedtest.net/")
time.sleep(1)

go_btn = driver.find_element(By.XPATH, "//span[@class='start-text']")
go_btn.click()
time.sleep(40)