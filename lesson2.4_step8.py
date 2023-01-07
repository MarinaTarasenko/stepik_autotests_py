#lesson2.4_step8

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #ждем пока цена не станет 100$
    browser.find_element(By.ID, "book").click()                      #кликаем забронировать
    time.sleep(1)
    x = browser.find_element(By.ID, "input_value").text
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    browser.find_element(By.ID, "solve").click()
    time.sleep(2)
    alert = browser.switch_to.alert                      #переходим на информационный алерт
    alert_text = alert.text                              #берем из него текст
    alert.accept()                                       #закрываем принятием
    print(alert_text)                                    #выводим сообщение из алерта на печать в консоль
finally:
    time.sleep(2)
    browser.quit()
