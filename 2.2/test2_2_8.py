import os
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    
    first_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control:nth-child(2)')
    first_name.send_keys('Дмитрий')

    last_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control:nth-child(4)')
    last_name.send_keys('Христодуло')

    email = browser.find_element(By.CSS_SELECTOR, 'input.form-control:nth-child(6)')
    email.send_keys('Khristdi@vk.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_name = "test.txt" 
    file_path = os.path.join(current_dir, 'test.txt')  
    element = browser.find_element(By.CSS_SELECTOR, '#file')         
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()