from datetime import datetime
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from base import BasePage
from config import API_CAPTCHA, invalid_captcha, valid_email_confirm, valid_phone_confirm


# локаторы сайта для страницы восстановления пароля
class RTPassRecLocators:
    LOCATOR_RT_PASS_REC_LINK = (By.ID, "forgot_password")
    LOCATOR_RT_PASS_REC_TYPE_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_RT_PASS_REC_TYPE_EMAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_RT_PASS_REC_TYPE_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_RT_PASS_REC_TYPE_LS = (By.ID, "t-btn-tab-ls")
    LOCATOR_RT_PASS_REC_LOGIN = (By.ID, "username")
    LOCATOR_RT_PASS_REC_CAPTCHA_IMG = (By.XPATH, "//img[@alt='Captcha']")
    LOCATOR_RT_PASS_REC_CAPTCHA_ANSWER = (By.ID, "captcha")
    LOCATOR_RT_PASS_REC_BUTTON_CONTINUE = (By.ID, "reset")
    LOCATOR_RT_PASS_REC_CODE_EMAIL = (By.XPATH, "//input[@value='email']//ancestor::label//span[@class='rt-radio__circle']")
    LOCATOR_RT_PASS_REC_CODE_PHONE = (By.XPATH, "//input[@value='sms']//ancestor::label//span[@class='rt-radio__circle']")
    LOCATOR_RT_PASS_REC_BUTTON_CONTINUE_RESET = \
        (By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded reset-choice-form__reset-btn']")
    LOCATOR_RT_PASS_REC_CODE_INPUT = (By.XPATH, "//input[@id='rt-code-0']")
    LOCATOR_RT_PASS_REC_NEW_PASSWORD = (By.ID, "password-new")
    LOCATOR_RT_PASS_REC_NEW_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    LOCATOR_RT_PASS_REC_BUTTON_SAVE_NEW_PASSWORD = (By.ID, "t-btn-reset-pass")


# локаторы сайта для проверки ожиданий со страницы восстановления пароля
    LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_TITLE = (By.CSS_SELECTOR, ".card-container__title")
    LOCATOR_RT_PASS_REC_EXPECT_LOGIN = (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")
    LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_FAIL = (By.ID, "form-error-message")
    LOCATOR_RT_PASS_REC_EXPECT_CODE_TITLE = (By.CSS_SELECTOR, ".card-container__title")
    LOCATOR_RT_PASS_REC_EXPECT_CODE_SEND = (By.CSS_SELECTOR, ".card-container__desc")
    LOCATOR_RT_PASS_REC_EXPECT_CODE_INVALID = (By.ID, "form-error-message")
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_FORM = (By.CSS_SELECTOR, ".card-container__desc")
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_IS_OLD = (By.ID, "form-error-message")
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_CONFIRM = (By.ID, "form-error-message")
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD = (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")
    LOCATOR_RT_PASS_REC_EXPECT_AUTH_NEW = (By.CSS_SELECTOR, ".card-container__title")


# тестовые методы для данных при восстановлении пароля
class PassRecRT(BasePage):
    def pass_rec_page(self):
        pass_rec_link = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_LINK)
        pass_rec_link.click()
        return pass_rec_link

    def pass_rec_type_phone(self):
        pass_rec_type_phone = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_PHONE)
        pass_rec_type_phone.click()
        return pass_rec_type_phone

    def pass_rec_type_email(self):
        pass_rec_type_email = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_EMAIL)
        pass_rec_type_email.click()
        return pass_rec_type_email

    def pass_rec_type_login(self):
        pass_rec_type_login = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_LOGIN)
        pass_rec_type_login.click()
        return pass_rec_type_login

    def pass_rec_type_ls(self):
        pass_rec_type_ls = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_LS)
        pass_rec_type_ls.click()
        return pass_rec_type_ls

    def pass_rec_login(self, login):
        pass_rec_login = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_LOGIN)
        pass_rec_login.click()
        pass_rec_login.clear()
        pass_rec_login.send_keys(login)
        return pass_rec_login

    def captcha(self):
        captcha_url = None
        if captcha_url == self.is_presented(RTPassRecLocators.LOCATOR_RT_PASS_REC_CAPTCHA_IMG) is None:
            pass
        else:
            captcha_url = self.is_presented(RTPassRecLocators.LOCATOR_RT_PASS_REC_CAPTCHA_IMG).get_attribute('src')

            def captcha_solution():
                solver = TwoCaptcha(API_CAPTCHA)
                result = solver.normal(captcha_url, caseSensitive=1)
                return result['code']

            captcha_answer = captcha_solution()
            # time.sleep(20)
            captcha_pass = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CAPTCHA_ANSWER)
            captcha_pass.click()
            captcha_pass.send_keys(captcha_answer)
            return captcha_pass

    def invalid_captcha(self):
        captcha_url = None
        if captcha_url == self.is_presented(RTPassRecLocators.LOCATOR_RT_PASS_REC_CAPTCHA_IMG) is None:
            pass
        else:
            captcha_pass = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CAPTCHA_ANSWER)
            captcha_pass.click()
            captcha_pass.send_keys(invalid_captcha)
            return captcha_pass

    def pass_rec_button_continue(self):
        pass_rec_button_continue = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_BUTTON_CONTINUE)
        pass_rec_button_continue.click()
        return pass_rec_button_continue

    def pass_rec_code_email(self):
        pass_rec_code_email = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_EMAIL)
        pass_rec_code_email.click()
        return pass_rec_code_email

    def pass_rec_code_phone(self):
        pass_rec_code_phone = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_PHONE)
        pass_rec_code_phone.click()
        return pass_rec_code_phone

    def pass_rec_button_continue_reset(self):
        pass_rec_button_continue_reset = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_BUTTON_CONTINUE_RESET)
        pass_rec_button_continue_reset.click()
        return pass_rec_button_continue_reset

    def pass_rec_code_input_invalid_code(self, email_code):
        pass_rec_code_input_invalid_code = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_INPUT)
        pass_rec_code_input_invalid_code.click()
        pass_rec_code_input_invalid_code.send_keys(email_code)
        return pass_rec_code_input_invalid_code

    def pass_rec_code_input_valid_code(self):
        pass_rec_code_input_valid_code = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_INPUT)
        pass_rec_code_input_valid_code.click()
        # ручной ввод кода, полученного на электронную почту или по смс
        return pass_rec_code_input_valid_code

    def pass_rec_new_password(self, password):
        pass_rec_form_new_password = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_NEW_PASSWORD)
        pass_rec_form_new_password.click()
        pass_rec_form_new_password.send_keys(password)
        return pass_rec_form_new_password

    def pass_rec_new_password_confirm(self, password_confirm):
        pass_rec_form_new_password_confirm = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_NEW_PASSWORD_CONFIRM)
        pass_rec_form_new_password_confirm.click()
        pass_rec_form_new_password_confirm.send_keys(password_confirm)
        return pass_rec_form_new_password_confirm

    def pass_rec_button_save_new_password(self):
        pass_rec_new_password_button_save = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_BUTTON_SAVE_NEW_PASSWORD)
        pass_rec_new_password_button_save.click()
        return pass_rec_new_password_button_save


# тестовые методы для проверки ожиданий и результатов при восстановлении пароля
class PassRecRTExpectations(BasePage):
    def pass_rec_expect_pass_rec_title(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_TITLE)
        pass_rec_expect_pass_rec_title = pass_rec_expect.text == "Восстановление пароля"
        return pass_rec_expect_pass_rec_title

    def pass_rec_expect_login(self):
        pass_rec_expect = None
        if pass_rec_expect == self.is_presented(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_LOGIN) is None:
            pass
        else:
            pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_LOGIN)
            pass_rec_expect_login = pass_rec_expect.text == "Введите номер телефона" or "Введите адрес, указанный при регистрации" \
                or "Введите логин, указанный при регистрации" or "Введите номер вашего лицевого счета" \
                or "Неверный формат телефона" or "Проверьте, пожалуйста, номер лицевого счета"
            return pass_rec_expect_login

    def pass_rec_expect_pass_rec_fail(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_FAIL)
        pass_rec_expect_code_invalid = pass_rec_expect.text == "Неверный логин или текст с картинки"
        return pass_rec_expect_code_invalid

    def pass_rec_expect_code_title(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_CODE_TITLE)
        pass_rec_expect_code_title = pass_rec_expect.text == "Восстановление пароля"
        return pass_rec_expect_code_title

    def pass_rec_expect_code_send(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_CODE_SEND)
        pass_rec_expect_code_send = pass_rec_expect.text == \
            f"Код подтверждения отправлен на адрес {valid_email_confirm}"\
            or f"Код подтверждения отправлен на номер {valid_phone_confirm}"
        return pass_rec_expect_code_send

    def pass_rec_expect_code_invalid(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_CODE_INVALID)
        pass_rec_expect_code_invalid = pass_rec_expect.text == "Неверный код. Повторите попытку"
        return pass_rec_expect_code_invalid

    def pass_rec_expect_new_password_form(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_FORM)
        pass_rec_expect_new_password_form = pass_rec_expect.text == "Новый пароль должен содержать от 8 до 20 знаков, " \
            "включать латинские, заглавные и строчные буквы, цифры или специальные символы"
        return pass_rec_expect_new_password_form

    def pass_rec_expect_new_password(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD)
        pass_rec_expect_new_password = pass_rec_expect.text == "Длина пароля должна быть не менее 8 символов" \
            or "Длина пароля должна быть не более 20 символов" or "Пароль должен содержать хотя бы одну заглавную букву"\
            or "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру" or "Пароли не совпадают" \
            or "Пароль должен содержать хотя бы одну прописную букву" or "Пароль должен содержать только латинские буквы"
        return pass_rec_expect_new_password

    def pass_rec_expect_new_password_is_old(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_IS_OLD)
        pass_rec_expect_new_password_is_old = pass_rec_expect.text == "Этот пароль уже использовался, укажите другой пароль"
        return pass_rec_expect_new_password_is_old

    def auth_expect_auth_new(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_AUTH_NEW)
        auth_expect_auth_new = pass_rec_expect.text == "Авторизация"
        return auth_expect_auth_new

    def timetest(self):
        now = datetime.now()
        timetest = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}"
        return timetest
