from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
import allure


class PersonalAccountPage(BasePage):
    @allure.step('Вход в аккаунт')
    def login_to_account(self, create_user):
        user_data, _, _ = create_user
        email = user_data["email"]
        password = user_data["password"]

        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        self.enter_text(PersonalAccountLocators.EMAIL, email)
        self.enter_text(PersonalAccountLocators.PASSWORD, password)
        self.click_element(PersonalAccountLocators.BUTTON_LOGIN)

    @allure.step('Клик по кнопке «Войти»')
    def click_button_account(self):
        self.wait_clickable_element(PersonalAccountLocators.BUTTON_LOGIN)
        self.click_element(PersonalAccountLocators.BUTTON_LOGIN)

    @allure.step('Ожидание кнопки «Профиль»')
    def wait_button_profile(self):
        self.wait_clickable_element(PersonalAccountLocators.PROFILE)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_button_personal_account(self):
        self.wait_clickable_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик кнопки «История заказов»')
    def click_history_order(self):
        self.wait_clickable_element(PersonalAccountLocators.BUTTON_ORDER_HISTORY)
        self.click_element(PersonalAccountLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Клик кнопки «Выход»')
    def click_exit(self):
        self.wait_clickable_element(PersonalAccountLocators.BUTTON_EXIT)
        self.click_element(PersonalAccountLocators.BUTTON_EXIT)

    @allure.step('Получить ссылку текущей страницы')
    def check_url(self):
        return self.get_url()
