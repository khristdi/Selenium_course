from distutils.spawn import find_executable
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

# считаем математическую функцию от х
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    print(y)

# скролим страницу вниз
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

# чекбокс и ответ
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

