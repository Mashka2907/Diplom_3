from selenium.webdriver.common.by import By


"""Локаторы для работы в личном кабинете"""
class PersonalAccountLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]') #Личный кабинет
    PROFILE = (By.XPATH, '//a[text() = "Профиль"]')  #Профиль
    EMAIL = (By.XPATH, '//input[@name="name"]')  #поле ввода email
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  #поле ввода password
    BUTTON_LOGIN = (By.XPATH, '//button[text() = "Войти"]') #кнопка Войти
    BUTTON_ORDER_HISTORY = (By.XPATH, '//a[text() = "История заказов"]')  #История заказов
    BUTTON_EXIT = (By.XPATH, '//button[text() = "Выход"]') #кнопка Выход
