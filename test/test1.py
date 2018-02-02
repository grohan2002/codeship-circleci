import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicit_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        #self.driver.get("http://orionlabs123.staging.wpengine.com/")
        self.driver.get("https://www.orionlabs.io/")


    #def test_example(self):
    #    self.driver.get("http://orionlabs123.staging.wpengine.com/")
    #    #self.assertEqual(self.driver.title, "menu-main-navigation-menu")
    #    self.assertEqual(self.driver.find_element_by_id("menu-main-navigation-menu"))
    #def tearDown(self):
    #    self.driver.quit()



    def shop-validate(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("menu-item-3084")

        # enter search keyword and submit
        #self.search_field.send_keys("Selenium WebDriver Interview questions")
        #self.search_field.submit()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod

        #lists = self.driver.find_elements_by_class_name("r")
        #no=len(lists)
        #self.assertEqual(11, len(lists))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
