import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class toolsqa(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()

    def test_filldetails(self):
        driver=self.driver
        driver.maximize_window()
        driver.get('http://www.toolsqa.com')
        driver.implicitly_wait(30)
        tt1=driver.find_element_by_link_text('ABOUT')
        tt1.click()
        WebDriverWait(driver,20).until(expected_conditions.title_contains('About '))
        driver.back()
        driver.forward()
        WebDriverWait(driver,20).until(expected_conditions.title_contains('About '))
        driver.back()
        driver.refresh()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
unittest.main()
