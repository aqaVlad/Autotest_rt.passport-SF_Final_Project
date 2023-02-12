from datetime import datetime
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from base import BasePage
from config import API_CAPTCHA, valid_first_name, valid_last_name, invalid_captcha


# локаторы сайта для страницы авторизации
class RTAuthLocators:
    LOCATOR_RT_AUTH_TYPE_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_RT_AUTH_TYPE_EMAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_RT_AUTH_TYPE_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_RT_AUTH_TYPE_LS = (By.ID, "t-btn-tab-ls")
    LOCATOR_RT_AUTH_LOGIN = (By.ID, "username")
    LOCATOR_RT_AUTH_PASSWORD = (By.ID, "password")
    LOCATOR_RT_AUTH_BUTTON = (By.ID, "kc-login")
    LOCATOR_RT_AUTH_CAPTCHA_IMG = (By.XPATH, "//img[@alt='Captcha']")
    LOCATOR_RT_AUTH_CAPTCHA_ANSWER = (By.ID, "captcha")

    # локаторы сайта для проверки ожиданий со страницы авторизации
    LOCATOR_RT_AUTH_EXPECT_SLOGAN = (By.CSS_SELECTOR, ".what-is__desc")
    LOCATOR_RT_AUTH_EXPECT_TITLE = (By.CSS_SELECTOR, ".card-container__title")
    LOCATOR_RT_AUTH_EXPECT_LOGIN = (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")
    LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL = (By.ID, "form-error-message")
    LOCATOR_RT_AUTH_EXPECT_AUTH_FAIL = (By.ID, "form-error-message")
    LOCATOR_RT_AUTH_EXPECT_AUTH_NAME = (By.CSS_SELECTOR, ".user-name__first-patronymic")
    LOCATOR_RT_AUTH_EXPECT_AUTH_SURNAME = (By.CSS_SELECTOR, ".user-name__last-name")


# тестовые методы для данных при авторизации
class AuthRT(BasePage):
    def auth_type_phone(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_PHONE)
        auth_type_phone.click()
        return auth_type_phone

    def auth_type_email(self):
        auth_type_email = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_EMAIL)
        auth_type_email.click()
        return auth_type_email

    def auth_type_login(self):
        auth_type_login = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_LOGIN)
        auth_type_login.click()
        return auth_type_login

    def auth_type_ls(self):
        auth_type_ls = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_LS)
        auth_type_ls.click()
        return auth_type_ls

    def auth_login(self, login):
        auth_form_name = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_LOGIN)
        auth_form_name.click()
        auth_form_name.clear()
        auth_form_name.send_keys(login)
        return auth_form_name

    def auth_password(self, password):
        auth_form_name = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_PASSWORD)
        auth_form_name.click()
        auth_form_name.send_keys(password)
        return auth_form_name

    def auth_button(self):
        auth_form_button = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_BUTTON)
        auth_form_button.click()
        return auth_form_button

    def captcha(self):
        captcha_url = None
        if captcha_url == self.is_presented(RTAuthLocators.LOCATOR_RT_AUTH_CAPTCHA_IMG) is None:
            pass
        else:
            captcha_url = self.is_presented(RTAuthLocators.LOCATOR_RT_AUTH_CAPTCHA_IMG).get_attribute('src')

            def captcha_solution():
                solver = TwoCaptcha(API_CAPTCHA)
                result = solver.normal(captcha_url, caseSensitive=1)
                return result['code']

            captcha_answer = captcha_solution()
            # time.sleep(20)
            captcha_pass = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_CAPTCHA_ANSWER)
            captcha_pass.click()
            captcha_pass.send_keys(captcha_answer)
            return captcha_pass

    def invalid_captcha(self):
        captcha_url = None
        if captcha_url == self.is_presented(RTAuthLocators.LOCATOR_RT_AUTH_CAPTCHA_IMG) is None:
            pass
        else:
            captcha_pass = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_CAPTCHA_ANSWER)
            captcha_pass.click()
            captcha_pass.send_keys(invalid_captcha)
            return captcha_pass


# тестовые методы для проверки ожиданий и результатов при авторизации
class AuthRTExpectations(BasePage):
    def auth_expect_auth_page(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_TITLE)
        auth_expect_title = auth_expect.text == "Авторизация"
        return auth_expect_title

    def auth_expect_auth_slogan(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_SLOGAN)
        auth_expect_slogan = auth_expect.text == "Персональный помощник в цифровом мире Ростелекома"
        return auth_expect_slogan

    def auth_expect_login(self):
        auth_expect = None
        if auth_expect == self.is_presented(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_LOGIN) is None:
            pass
        else:
            auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_LOGIN)
            auth_expect_login = auth_expect.text == "Введите номер телефона" or "Введите адрес, указанный при регистрации" \
                or "Введите логин, указанный при регистрации" or "Введите номер вашего лицевого счета" \
                or "Неверный формат телефона" or "Проверьте, пожалуйста, номер лицевого счета"
            return auth_expect_login

    def auth_expect_captcha_fail(self):
        auth_expect = None
        if auth_expect == self.is_presented(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL) is None:
            pass
        else:
            auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL)
            auth_expect_captcha_fail = auth_expect.text == "Неверно введен текст с картинки"
            return auth_expect_captcha_fail

    def auth_expect_auth_fail(self):
        auth_expect = None
        if auth_expect == self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_FAIL) is None:
            pass
        else:
            auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_FAIL)
            auth_expect_auth_fail = auth_expect.text == "Неверный логин или пароль"
            return auth_expect_auth_fail

    def auth_expect_name(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_NAME)
        auth_expect_name = auth_expect.text == valid_first_name
        return auth_expect_name

    def auth_expect_surname(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_SURNAME)
        auth_expect_surname = auth_expect.text == valid_last_name
        return auth_expect_surname

    def timetest(self):
        now = datetime.now()
        timetest = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}"
        return timetest
