# python -m pytest -v --driver Edge --driver-path edgedriver.exe test_rt_pass_rec.py


import time
import pytest
from rt_passport_pass_rec import PassRecRT, PassRecRTExpectations

from config import valid_email, invalid_email, unicode_password, long_password, short_password, only_letter_password,\
    lower_password, upper_password, cyrillic_password, empty_form, invalid_code, invalid_phone, valid_phone,\
    new_valid_password, invalid_phone_2, new_valid_password_confirm, non_reg_email, non_reg_phone, digit_valid_email,\
    non_reg_ls, invalid_ls, non_reg_login, old_valid_password, old_valid_password_confirm


# Позитивный тест загрузки страницы и перехода в раздел Восстановления пароля
# ТЕСТ 3-01 - переход на страницу Восстановления пароля со страницы Авторизации
def test_pass_rec_page(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_pass_rec_title()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# Позитивные тесты способов восстановления пароля по зарегистрированным данных
# ТЕСТ 3-02 - ввод данных в форму Восстановления пароля - по номеру телефона и по смс-коду
def test_pass_rec_valid_phone_phone(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_phone()
    rt_passport_pass_rec_page.pass_rec_login(valid_phone)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_phone()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()
    rt_passport_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    rt_passport_pass_rec_page.pass_rec_new_password(new_valid_password)
    rt_passport_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    rt_passport_pass_rec_page.pass_rec_button_save_new_password()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-03 - ввод данных в форму Восстановления пароля - по номеру телефона и по коду на E-mail
def test_pass_rec_valid_phone_email(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_phone()
    rt_passport_pass_rec_page.pass_rec_login(valid_phone)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_email()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()
    rt_passport_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    rt_passport_pass_rec_page.pass_rec_new_password(new_valid_password)
    rt_passport_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    rt_passport_pass_rec_page.pass_rec_button_save_new_password()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-04 - ввод данных в форму Восстановления пароля - по E-mail и по смс-коду
def test_pass_rec_valid_email_phone(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_phone()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()
    rt_passport_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    rt_passport_pass_rec_page.pass_rec_new_password(new_valid_password)
    rt_passport_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    rt_passport_pass_rec_page.pass_rec_button_save_new_password()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-05 - ввод данных в форму Восстановления пароля - по E-mail и по коду на E-mail
def test_pass_rec_valid_email_email(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_email()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()
    rt_passport_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    rt_passport_pass_rec_page.pass_rec_new_password(new_valid_password)
    rt_passport_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    rt_passport_pass_rec_page.pass_rec_button_save_new_password()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# негативные тесты ввода невалидных данных по каждому отдельному полю
# ТЕСТ 3-06 (x10 параметров) - ввод данных в форму Восстановления пароля - по номеру телефона, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_phone(browser, login, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_phone()
    rt_passport_pass_rec_page.pass_rec_login(login)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_login or rt_passport_pass_rec_page.pass_rec_expect_pass_rec_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-07 (x10 параметров) - ввод данных в форму Восстановления пароля - по E-mail, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_email(browser, login, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(login)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_login or rt_passport_pass_rec_page.pass_rec_expect_pass_rec_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-08 (x10 параметров) - ввод данных в форму Восстановления пароля - по Логину, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_login(browser, login, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_login()
    rt_passport_pass_rec_page.pass_rec_login(login)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_login or rt_passport_pass_rec_page.pass_rec_expect_pass_rec_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-09 (x10 параметров) - ввод данных в форму Восстановления пароля - по лицевому счету, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_ls(browser, login, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_ls()
    rt_passport_pass_rec_page.pass_rec_login(login)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_login or rt_passport_pass_rec_page.pass_rec_expect_pass_rec_fail()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-10 - ввод данных в форму Восстановления пароля - без выбора варианта получения кода
def test_pass_rec_form_valid_login_by_none(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_code_send()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-11 - ввод данных в форму Восстановления пароля
# выбор получения кода по E-mail, ввод неверного кода
def test_pass_rec_form_valid_login_by_code(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_email()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_code_send()

    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.pass_rec_code_input_invalid_code(invalid_code)

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_code_send()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-12 - ввод данных в форму Восстановления пароля
# выбор получения кода по смс, ввод неверного кода
def test_pass_rec_form_valid_login_by_sms(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_phone()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_code_send()

    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.pass_rec_code_input_invalid_code(invalid_code)

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_code_send()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-13 (x8 параметров) - ввод данных в форму Восстановления пароля - Поле "Пароль"
@pytest.mark.parametrize("password", [unicode_password, short_password, long_password, empty_form,
                                      only_letter_password, lower_password, upper_password, cyrillic_password])
def test_pass_rec_form_new_password(browser, password, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_phone()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()
    rt_passport_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_new_password_form()

    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.pass_rec_new_password(password)
    rt_passport_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    rt_passport_pass_rec_page.pass_rec_button_save_new_password()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_new_password()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-14 (x8 параметров) - ввод данных в форму Восстановления пароля - Поле "Подтверждение пароля"
@pytest.mark.parametrize("password_confirm", [unicode_password, short_password, long_password, empty_form,
                                only_letter_password, lower_password, upper_password, cyrillic_password])
def test_pass_rec_form_new_password_confirm(browser, password_confirm, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_phone()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()
    rt_passport_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_new_password_form()

    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.pass_rec_new_password(new_valid_password)
    rt_passport_pass_rec_page.pass_rec_new_password_confirm(password_confirm)
    rt_passport_pass_rec_page.pass_rec_button_save_new_password()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_new_password()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')


# ТЕСТ 3-15 - ввод данных в форму Восстановления пароля - Поля "Пароль" и "Подтверждение пароля"
# ввод ранее использованного валидного пароля в качестве нового пароля
def test_pass_rec_form_new_password_is_old(browser, request):
    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.go_to_site()
    rt_passport_pass_rec_page.pass_rec_page()
    rt_passport_pass_rec_page.pass_rec_type_email()
    rt_passport_pass_rec_page.pass_rec_login(valid_email)
    rt_passport_pass_rec_page.captcha()
    rt_passport_pass_rec_page.pass_rec_button_continue()
    rt_passport_pass_rec_page.pass_rec_code_phone()
    rt_passport_pass_rec_page.pass_rec_button_continue_reset()
    rt_passport_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_new_password_form()

    rt_passport_pass_rec_page = PassRecRT(browser)
    rt_passport_pass_rec_page.pass_rec_new_password(old_valid_password)
    rt_passport_pass_rec_page.pass_rec_new_password_confirm(old_valid_password_confirm)
    rt_passport_pass_rec_page.pass_rec_button_save_new_password()

    rt_passport_pass_rec_page = PassRecRTExpectations(browser)
    assert rt_passport_pass_rec_page.pass_rec_expect_new_password_is_old()
    browser.save_screenshot(f'screenshots/{request.node.name}_{rt_passport_pass_rec_page.timetest()}.png')
