import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Base_test(unittest.TestCase):
    def setUp(self):
        self.valor = 10
        self.rest = 15

    def tearDown(self):
        pass

    def test_suma(self):
        result = 5 + 7
        self.assertNotEqual(result,self.valor,'NO')

    def test_resta(self):
        result = 20 - 5
        self.assertEqual(result,self.rest)

if __name__ == '__main__':
    unittest.main()
