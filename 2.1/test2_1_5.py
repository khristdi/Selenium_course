import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)  


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option2.click()
    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

