# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class BuildFormsTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://orionlabs124.staging.wpengine.com/"


    def test_LearnMore1_link(self):
        driver = self.driver
        print("----- CLick on the first Learn More link and traverse the About Us Page-----------------")
        driver.get('http://orionlabs124:b37e44da@orionlabs124.staging.wpengine.com/')
        driver.find_element_by_xpath('//*[@id="features"]/div/p[2]/a/button').click()
        driver.find_element_by_xpath('//*[@id="menu-item-43"]/a').click()
        #print (driver.title) - About Orion Labs - Founders, Investors, and Management Team
        self.assertIn("Founders", driver.title)


    def test_LearnMore2_link(self):
        driver = self.driver
        print("----- CLick on the Second Learn More link and traverse the Careers  & User Guide Page----------------")
        driver.get('http://orionlabs124:b37e44da@orionlabs124.staging.wpengine.com/')
        driver.find_element_by_xpath('//*[@id="green-blue"]/div/div[1]/div[3]/a/button').click()
        driver.find_element_by_xpath('//*[@id="menu-item-3420"]/a').click()
        self.assertIn("welcome", driver.title)
        driver.find_element_by_xpath('//*[@id="menu-item-1829"]/a').click()
        self.assertIn("Guide", driver.title)

    def test_LearnMore3_link(self):
        driver = self.driver
        print("----- CLick on the Third Learn More link-----------------")
        driver.get('http://orionlabs124:b37e44da@orionlabs124.staging.wpengine.com/')
        driver.find_element_by_xpath('//*[@id="green-blue"]/div/div[2]/div[3]/a/button').click()


    def tearDown(self):
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
