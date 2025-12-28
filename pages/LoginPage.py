from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_QR_BUTTON = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    CANNOT_LOGIN_BUTTON = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTER_BUTTON = (By.XPATH, '//button[.//text()="Зарегистрироваться"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAILRU_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')

class LoginPageHelper:
    pass
    