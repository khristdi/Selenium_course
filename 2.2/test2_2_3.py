import math
import select
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
import time


try:

    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link) 

    x = browser.find_element(By.CSS_SELECTOR, '#num1')
    xt = x.text
    y = browser.find_element(By.CSS_SELECTOR, '#num2')
    yt = y.text
    z = str(int(xt) + int(yt))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

