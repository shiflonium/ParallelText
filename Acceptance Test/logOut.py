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
        Select(driver.find_element_by_id("id_native_lang")).select_by_visible_text("Spanish")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("exdx")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("exdx")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Account").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("exdx")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("exdx")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()s