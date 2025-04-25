import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class RetoUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_element_UserName(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()

        try:
            usernamefield = self.driver.find_element(By.XPATH,"//input[@id='user-name']")
        except NoSuchElementException:
            self.fail("No se encontró el elemento")
        self.assertTrue(usernamefield.is_displayed())

        #loginBtn = self.driver.find_element(By.XPATH,"//input[@id='login-buttons']")
        #self.assertTrue(len(loginBtn)>0), f"No se encontró ningún elemento"
    def test_element_Password(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        passwordField = self.driver.find_elements(By.XPATH, "//input[@id='password']")
        self.assertTrue(len(passwordField) > 0), "No se encontró ningún elemento"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()