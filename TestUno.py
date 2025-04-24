import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Create an object from Options class
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Tip

usuarioUno = "Ricardo"
email_userUno = "richardram233@gmail.com"

# 2. Driver init
driver = webdriver.Chrome(options=chrome_options)

# 3. Start the automated flow
driver.get("https://demoqa.com/text-box")

# 4. Actions
time.sleep(2)

#nom = driver.find_element(By.XPATH, "//input[@id='userName']")

wait = WebDriverWait(driver,10)
nom = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='userName']")))
nom.send_keys(usuarioUno)

time.sleep(2)

email_input = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email_input.send_keys(email_userUno)

time.sleep(3)
nom.clear()
email_input.clear()
time.sleep(1)

driver.close()
