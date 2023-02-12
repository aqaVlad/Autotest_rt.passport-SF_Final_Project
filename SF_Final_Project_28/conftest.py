import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""Тесты написаны для браузера Edge.
В случае запуска тестов на другом браузере укажите его название в фикстуре ниже,
 а также пропишите путь до соответствующего драйвера браузера WebDriver"""


# фикстура открывает браузер и запускает веб-драйвер
"""для регистрации оптимальнее использовать scope="session"
для авторизации и восстановления пароля оптимальнее использовать scope="function",
чтобы сбрасывались предыдущие введенные данные и входы в ЛК"""
@pytest.fixture(scope="function")
def browser():
    s = Service("edgedriver.exe")
    driver = webdriver.Edge(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
