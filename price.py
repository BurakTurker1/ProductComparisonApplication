import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
item_name = input("enter your item name: ")
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_something(self):
        driver = self.driver
        driver.get("https://www.trendyol.com/")
        search_bar = driver.find_element(By.CLASS_NAME, "V8wbcUhU")
        search_bar.send_keys(item_name)
        search_bar.send_keys(Keys.ENTER)
        prices = driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "prc-box-dscntd")))
        for element in prices:
            print(element.text)
        time.sleep(25)


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
