from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class ReadBooksInParallel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://parallel-text.herokuapp.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_read_books_in_parallel(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Parallel Text").click()
        driver.find_element_by_link_text("Parallel Text").click()
        driver.find_element_by_link_text("Read Books").click()
        driver.find_element_by_name("book_submit").click()
        Select(driver.find_element_by_id("id_left_lang_dd")).select_by_visible_text("Arabic")
        driver.find_element_by_name("chap_lang_submit").click()
    
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
