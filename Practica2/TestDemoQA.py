import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDemoQA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_textbox(self):
        self.driver.get("https://demoqa.com/text-box")
        campo = self.driver.find_element(By.ID, "userName")
        campo.send_keys("Ricardo")
        self.assertEqual(campo.get_attribute("value"), "Ricardo")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
