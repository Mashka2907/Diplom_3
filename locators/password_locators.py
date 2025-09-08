from selenium.webdriver.common.by import By


"""Локаторы для восстановления пароля."""
class PasswordLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]') #Личный кабинет
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]') #кнопка Восстановить пароль
    BUTTON_RESTORE = (By.XPATH, '//button[text()="Восстановить"]') #кнопка Восстановить
    EMAIL = (By.XPATH, '//input[@name="name"]') #поле ввода email
    ICON_ACTION_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') #раскрыть пароль
    NEW_PASSWORD = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::*') #поле ввода пароля
    BUTTON_SAVE = (By.XPATH, '//button[text()="Сохранить"]') #кнопка Сохранить


