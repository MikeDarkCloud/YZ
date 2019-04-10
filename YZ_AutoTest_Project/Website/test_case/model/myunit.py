import unittest
import driver

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=driver.browser()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()