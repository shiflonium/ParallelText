'''Acceptance test for logout successfully feature.
This tests the system when someone tries to logout
and they successfully able to do so and re-sign back again.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Logout(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.base_url = "http://lit-earth-8332.herokuapp.com/"
            self.verificationErrors = []
            self.accept_next_alert = True
    
        def test_logout(self):
            driver = self.driver
            driver.get(self.base_url + "/#")
            driver.find_element_by_link_text("Register").click()
            driver.find_element_by_id("id_username").clear()
            driver.find_element_by_id("id_username").send_keys("exdx")
            driver.find_element_by_id("id_password1").clear()
            driver.find_element_by_id("id_password1").send_keys("exdx")
            driver.find_element_by_id("id_password2").clear()
            driver.find_element_by_id("id_password2").send_keys("exdx")
        
        






if __name__ == "__main__":
    unittest.main()