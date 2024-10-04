from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.first")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third")

        first_name.send_keys("Имя")
        last_name.send_keys("Фамилия")
        email.send_keys("test@example.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
        button.click()

        time.sleep(1)
    finally:
        browser.quit()

# Тестирование первой страницы (регистрация должна пройти успешно)
test_registration("http://suninjuly.github.io/registration1.html")

# Тестирование второй страницы (ожидаем ошибку NoSuchElementException)
test_registration("http://suninjuly.github.io/registration2.html")

#использую браузер хром