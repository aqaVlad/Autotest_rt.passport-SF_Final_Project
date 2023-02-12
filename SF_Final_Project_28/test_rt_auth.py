# python -m pytest -v --driver Edge --driver-path edgedriver.exe test_rt_auth.py

import time
import pytest
from rt_passport_auth import AuthRT, AuthRTExpectations

from config import valid_password, valid_phone, valid_email, digit_valid_email, invalid_email, invalid_password, \
    non_reg_email, invalid_phone, non_reg_phone, non_reg_login, non_reg_ls, invalid_ls, invalid_phone_2, empty_form


# Позитивный тест загрузки страницы Авторизации
# ТЕСТ 2-01 - загрузка страницы Авторизации и наличие корпоративного слогана
def test_auth_page(browser, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_auth_page()
    assert rt_passport_auth_page.auth_expect_auth_slogan()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# Позитивные тесты входа в зарегистрированный ЛК разными способами (по доступности) с верными данными
# ТЕСТ 2-02 - вход через форму Авторизации с использованием E-mail
def test_auth_email_valid_form(browser, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_email()
    rt_passport_auth_page.auth_login(valid_email)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.captcha()
    # time.sleep(20)
    rt_passport_auth_page.auth_button()
    time.sleep(10)

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_name()
    assert rt_passport_auth_page.auth_expect_surname()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# ТЕСТ 2-03 - вход через форму Авторизации с использованием номера телефона
def test_auth_phone_valid_form(browser, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_phone()
    rt_passport_auth_page.auth_login(valid_phone)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.captcha()
    rt_passport_auth_page.auth_button()
    time.sleep(10)

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_name()
    assert rt_passport_auth_page.auth_expect_surname()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# 50/50 позитивно-негативные тесты (зависит от появления captcha):
# ввод в captcha невалидных данных при прочих валидных данных
# ТЕСТ 2-04 - вход через форму Авторизации с использованием E-mail
def test_auth_email_valid_form_invalid_captcha(browser, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_email()
    rt_passport_auth_page.auth_login(valid_email)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.invalid_captcha()
    rt_passport_auth_page.auth_button()
    time.sleep(10)

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert (rt_passport_auth_page.auth_expect_name() and rt_passport_auth_page.auth_expect_surname())\
           or rt_passport_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# ТЕСТ 2-05 - вход через форму Авторизации с использованием номера телефона
def test_auth_phone_valid_form_invalid_captcha(browser, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_phone()
    rt_passport_auth_page.auth_login(valid_phone)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.invalid_captcha()
    rt_passport_auth_page.auth_button()
    time.sleep(10)

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert (rt_passport_auth_page.auth_expect_name() and rt_passport_auth_page.auth_expect_surname())\
           or rt_passport_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# негативные тесты с вводом неверного пароля при валидном логине
# ТЕСТ 2-06 - вход через форму Авторизации по номеру телефона с использованием неверного пароля
def test_auth_phone_invalid_password(browser, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_phone()
    rt_passport_auth_page.auth_login(valid_phone)
    rt_passport_auth_page.auth_password(invalid_password)
    rt_passport_auth_page.captcha()
    rt_passport_auth_page.auth_button()

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_auth_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# ТЕСТ 2-07 - вход через форму Авторизации по E-mail с использованием неверного пароля
def test_auth_email_invalid_password(browser, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_email()
    rt_passport_auth_page.auth_login(valid_email)
    rt_passport_auth_page.auth_password(invalid_password)
    rt_passport_auth_page.captcha()
    rt_passport_auth_page.auth_button()

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_auth_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# негативные тесты с вводом несоответствующих типу поля данных / невалидных данных по каждому отдельному полю
# ТЕСТ 2-08 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по номеру телефона
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_phone_invalid_login(browser, login, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_phone()
    rt_passport_auth_page.auth_login(login)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.captcha()
    rt_passport_auth_page.auth_button()

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_login() or rt_passport_auth_page.auth_expect_auth_fail() \
           or rt_passport_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# ТЕСТ 2-09 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по E-mail
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_email_invalid_login(browser, login, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_email()
    rt_passport_auth_page.auth_login(login)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.captcha()
    rt_passport_auth_page.auth_button()

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_login() or rt_passport_auth_page.auth_expect_auth_fail() \
           or rt_passport_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# ТЕСТ 2-10 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по логину
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_login(browser, login, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_login()
    rt_passport_auth_page.auth_login(login)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.captcha()
    rt_passport_auth_page.auth_button()

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_login() or rt_passport_auth_page.auth_expect_auth_fail() \
           or rt_passport_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')


# ТЕСТ 2-11 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по лицевому счету (ЛС)
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_ls(browser, login, request):
    rt_passport_auth_page = AuthRT(browser)
    rt_passport_auth_page.go_to_site()
    rt_passport_auth_page.auth_type_ls()
    rt_passport_auth_page.auth_login(login)
    rt_passport_auth_page.auth_password(valid_password)
    rt_passport_auth_page.captcha()
    rt_passport_auth_page.auth_button()

    rt_passport_auth_page = AuthRTExpectations(browser)
    assert rt_passport_auth_page.auth_expect_login() or rt_passport_auth_page.auth_expect_auth_fail() \
           or rt_passport_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_auth_page.timetest()}.png')
