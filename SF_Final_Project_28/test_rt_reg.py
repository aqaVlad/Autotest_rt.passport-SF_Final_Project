# python -m pytest -v --driver Edge --driver-path edgedriver.exe test_rt_reg.py

import pytest
from rt_passport_reg import RegRT, RegRTExpectations

from config import valid_first_name, valid_last_name, valid_password, valid_code, \
    valid_password_confirm, double_first_name, double_last_name, one_letter_first_name, one_letter_last_name, \
    double_dash_first_name, double_dash_last_name, apostrophe_first_name, apostrophe_last_name, latin_first_name, \
    latin_last_name, long_first_name, long_last_name, valid_email, invalid_email, unicode_password, long_password, \
    short_password, only_letter_password, lower_password, upper_password, cyrillic_password, invalid_password_confirm, \
    empty_form, invalid_code, valid_email_reg, invalid_phone, invalid_phone_2


# Позитивный тест загрузки страницы и перехода в раздел Регистрация
# ТЕСТ 1-01 - переход на страницу Регистрации со страницы Авторизации
def test_reg_page(browser, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_reg_title()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# Позитивный тест ввода всех валидных данных по каждому полю
# ТЕСТ 1-02 - ввод данных в форму Регистрации
def test_reg_form_valid(browser, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(valid_first_name)
    rt_passport_reg_page.reg_last_name(valid_last_name)
    rt_passport_reg_page.reg_address(valid_email)
    rt_passport_reg_page.reg_password(valid_password)
    rt_passport_reg_page.reg_password_confirm(valid_password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_valid_code()

    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.reg_code(valid_code)

    rt_passport_reg_page = RegRTExpectations(browser)
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# негативные тесты ввода невалидных данных по каждому отдельному полю
# ТЕСТ 1-03 (x7 параметров) - ввод данных в форму Регистрации - Поле "Имя"
@pytest.mark.parametrize("first_name", [double_first_name, one_letter_first_name, empty_form, double_dash_first_name,
                                        apostrophe_first_name, latin_first_name, long_first_name])
def test_reg_form_name(browser, first_name, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(first_name)
    rt_passport_reg_page.reg_last_name(valid_last_name)
    rt_passport_reg_page.reg_address(valid_email)
    rt_passport_reg_page.reg_password(valid_password)
    rt_passport_reg_page.reg_password_confirm(valid_password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_name()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# ТЕСТ 1-04 (x7 параметров) - ввод данных в форму Регистрации - Поле "Фамилия"
@pytest.mark.parametrize("last_name", [double_last_name, one_letter_last_name, double_dash_last_name,
                                       apostrophe_last_name, latin_last_name, long_last_name, empty_form])
def test_reg_form_surname(browser, last_name, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(valid_first_name)
    rt_passport_reg_page.reg_last_name(last_name)
    rt_passport_reg_page.reg_address(valid_email)
    rt_passport_reg_page.reg_password(valid_password)
    rt_passport_reg_page.reg_password_confirm(valid_password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_surname()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# ТЕСТ 1-05 (x4 параметра) - ввод данных в форму Регистрации - Поле "E-mail или мобильный телефон"
@pytest.mark.parametrize("address", [invalid_email, empty_form, invalid_phone, invalid_phone_2])
def test_reg_form_address(browser, address, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(valid_first_name)
    rt_passport_reg_page.reg_last_name(valid_last_name)
    rt_passport_reg_page.reg_address(address)
    rt_passport_reg_page.reg_password(valid_password)
    rt_passport_reg_page.reg_password_confirm(valid_password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_address()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# ТЕСТ 1-06 (x8 параметров) - ввод данных в форму Регистрации - Поле "Пароль"
@pytest.mark.parametrize("password", [unicode_password, short_password, long_password, empty_form,
                                      only_letter_password, lower_password, upper_password, cyrillic_password])
def test_reg_form_password(browser, password, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(valid_first_name)
    rt_passport_reg_page.reg_last_name(valid_last_name)
    rt_passport_reg_page.reg_address(valid_email)
    rt_passport_reg_page.reg_password(password)
    rt_passport_reg_page.reg_password_confirm(valid_password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_password()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# ТЕСТ 1-07 (x2 параметра) - ввод данных в форму Регистрации - Поле "Подтверждение пароля"
@pytest.mark.parametrize("password_confirm", [invalid_password_confirm, empty_form],
                         ids=["invalid_password_confirm", "empty_form"])
def test_reg_form_password_confirm(browser, password_confirm, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(valid_first_name)
    rt_passport_reg_page.reg_last_name(valid_last_name)
    rt_passport_reg_page.reg_address(valid_email)
    rt_passport_reg_page.reg_password(valid_password)
    rt_passport_reg_page.reg_password_confirm(password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_password_confirm()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# ТЕСТ 1-08 - ввод данных в форму Регистрации - Поле "Подтверждение email"
def test_reg_invalid_code(browser, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(valid_first_name)
    rt_passport_reg_page.reg_last_name(valid_last_name)
    rt_passport_reg_page.reg_address(valid_email)
    rt_passport_reg_page.reg_password(valid_password)
    rt_passport_reg_page.reg_password_confirm(valid_password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_code_send()
    browser.save_screenshot(f'screenshots/{request.node.name}.png')

    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.reg_code(invalid_code)

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_code_invalid()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')


# ТЕСТ 1-09 - ввод данных в форму Регистрации - Зарегистрированный ранее "E-mail или мобильный телефон"
def test_reg_address_reg(browser, request):
    rt_passport_reg_page = RegRT(browser)
    rt_passport_reg_page.go_to_site()
    rt_passport_reg_page.reg_page()
    rt_passport_reg_page.reg_first_name(valid_first_name)
    rt_passport_reg_page.reg_last_name(valid_last_name)
    rt_passport_reg_page.reg_address(valid_email_reg)
    rt_passport_reg_page.reg_password(valid_password)
    rt_passport_reg_page.reg_password_confirm(valid_password_confirm)
    rt_passport_reg_page.reg_button()

    rt_passport_reg_page = RegRTExpectations(browser)
    assert rt_passport_reg_page.reg_expect_address_reg()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_reg_page.timetest()}.png')
