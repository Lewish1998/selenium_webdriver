from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class WebTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_send_contact_message(self):
        driver = self.driver
        
        driver.get("https://lewis-halstead.co.uk")
        self.assertIn("Lewis Halstead", driver.title)

        contact = driver.find_element(By.LINK_TEXT, "Contact")
        contact.click()
        form = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/form[1]")
        self.assertTrue(form)
        
        name = driver.find_element(By.ID, "contactName")
        email = driver.find_element(By.ID, "contactEmail")
        subject = driver.find_element(By.ID, "contactSubject")
        message = driver.find_element(By.ID, "contactMessage")

        name.clear()
        name.send_keys("Testing Selenium")
        email.clear()
        email.send_keys("testing@mail.com")
        subject.clear()
        subject.send_keys("Testing selenium")
        message.clear()
        message.send_keys("This is testing the form in my website using python and selenium")
        form.submit()
        time.sleep(3)
        self.assertTrue(name.get_attribute("value") == "")
        
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()
