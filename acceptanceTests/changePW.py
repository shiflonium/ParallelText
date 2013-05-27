from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class ChangePW(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://parallel-text.herokuapp.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_change_p_w(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Parallel Text").click()
        driver.find_element_by_link_text("Welcome, emdad").click()
        driver.find_element_by_link_text("Change Password").click()
        driver.find_element_by_id("id_pass_old").clear()
        driver.find_element_by_id("id_pass_old").send_keys("emdad")
        driver.find_element_by_id("id_pass_new1").clear()
        driver.find_element_by_id("id_pass_new1").send_keys("ahmed")
        driver.find_element_by_id("id_pass_new2").clear()
        driver.find_element_by_id("id_pass_new2").send_keys("ahmed")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Parallel Text").click()
    
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
    unittest.main()
