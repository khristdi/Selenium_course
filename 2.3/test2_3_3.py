import time
import math
from selenium.webdriver.support.select import Select
from selenium import webdriver 
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    journey = browser.find_element(By.CSS_SELECTOR, '.btn')
    journey.click()
    confirm = browser.switch_to.alert
    confirm.accept()


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

