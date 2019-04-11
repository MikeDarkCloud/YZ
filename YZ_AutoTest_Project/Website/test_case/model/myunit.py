import unittest
from browser import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()