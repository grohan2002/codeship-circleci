from selenium import webdriver
import unittest
import sys

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()
        #self.driver.get("https://www.orionlabs.io/")
        self.driver.get("http://orionlabs123.staging.wpengine.com/")

    def test_search_by_text(self):
        assert "Smart" in self.driver.title
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
