import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class test_class_name(unittest.TestCase):
    def test_abs1(self):
        self.driver = webdriver.Chrome()
        driver = self.driver

        driver.get('http://suninjuly.github.io/registration1.html')
        input1 = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = driver.find_element(By.CSS_SELECTOR, ".third")
        input2.send_keys("Petrov")
        input3 = driver.find_element(By.CSS_SELECTOR, ".second_block > div:nth-child(1) > input:nth-child(2)")
        input3.send_keys("email")
        input4 = driver.find_element(By.CSS_SELECTOR, ".second")
        input4.send_keys("sdf")
        input5 = driver.find_element(By.CSS_SELECTOR, ".second_block > div:nth-child(2) > input:nth-child(2)")
        input5.send_keys("sdf")
        
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            'Congratulations! You have successfully registered!', welcome_text, 'Congratulations! You have successfully registered!'
        )

    def test_abs2(self):
        self.driver = webdriver.Chrome()
        driver = self.driver

        driver.get('http://suninjuly.github.io/registration2.html')
        input1 = driver.find_element(By.CSS_SELECTOR, ".first")
        input1.send_keys("Ivan")
        input2 = driver.find_element(By.CSS_SELECTOR, ".third")
        input2.send_keys("Petrov")
        input3 = driver.find_element(By.CSS_SELECTOR, ".second")
        input3.send_keys("email")
        input4 = driver.find_element(By.CSS_SELECTOR, ".second")
        input4.send_keys("sdf")
        
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            'Congratulations! You have successfully registered!', welcome_text, 'Congratulations! You have successfully registered!'
        )


if __name__ == "__main__": 
        unittest.main()

