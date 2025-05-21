import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

#PRUEBA FUNCIONAL DE INTERFAZ DE USUARIO (END TO END) AUTOMATIZADA CON SELENIUM

class RetoUnitTest(unittest.TestCase):

    def initPage(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_logo(self):
        self.initPage()
        try:
            logo = self.driver.find_element(By.XPATH,"//div[@class='login_logo']")
        except NoSuchElementException:
            self.fail("No se encontró el elemento")
        self.assertTrue(logo.is_displayed())

    def test_element_UserName(self):
        self.initPage()
        try:
            usernamefield = self.driver.find_element(By.XPATH,"//input[@id='user-name']")
        except NoSuchElementException:
            self.fail("No se encontró el elemento")
        self.assertTrue(usernamefield.is_displayed())

    def test_element_Password(self):
        self.initPage()
        passwordField = self.driver.find_elements(By.XPATH, "//input[@id='password']")
        self.assertTrue(len(passwordField) > 0), "No se encontró ningún elemento"

    def test_login_btn(self):
        self.initPage()
        try:
            loginBtn = self.driver.find_element(By.XPATH,"//input[@id='login-button']")
        except NoSuchElementException:
            self.fail("No se encontró el elemento")
        self.assertTrue(loginBtn.is_displayed())

    def test_login(self):
        try:
            self.initPage()
            userName= "standard_user"
            password= "secret_sauce"

            usernamefield = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
            usernamefield.clear()
            usernamefield.send_keys(userName)

            passwordField = self.driver.find_element(By.XPATH, "//input[@id='password']")
            passwordField.clear()
            passwordField.send_keys(password)

            loginBtn = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
            loginBtn.click()

            current_url = self.driver.current_url
            self.assertIn("/inventory.html", current_url, f"Después del Login debe ir a ´/inventory.html´  {current_url}")

        except NoSuchElementException:
            self.fail("No se inició sesion con exito")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()