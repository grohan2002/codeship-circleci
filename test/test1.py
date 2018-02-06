from selenium import webdriver
import unittest
import sys

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()
        self.base_url = "http://orionlabs123.staging.wpengine.com/"
        #self.driver.get("https://www.orionlabs.io/")
        #self.driver.get("http://rohanhgupta.wpengine.com")

    def home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        assert "Smart" in self.driver.title
    def test_shop(self):
        driver = self.driver
        driver.get(self.base_url + "/shop")
        assert "Walkie-Talkies" in self.driver.title

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
