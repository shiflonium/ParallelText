from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class UpdateInfo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://parallel-text.herokuapp.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_update_info(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Sign Up").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("exdx")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("exdx")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("exdx")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("emdadnrn@gmail.com")
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Emdad")
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Ahmed")
        Select(driver.find_element_by_id("id_native_lang")).select_by_visible_text("Bengali")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("exdx")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("exdx")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Welcome, exdx").click()
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("emdadnrn@yahoo.com")
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Ahmed")
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Emdad")
        Select(driver.find_element_by_id("id_native_lang")).select_by_visible_text("Bashkir")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Welcome, exdx").click()
        driver.find_element_by_link_text("Parallel Text").click()
        driver.find_element_by_link_text("Welcome,").click()
    
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
