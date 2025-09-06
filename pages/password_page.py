from pages.base_page import BasePage
from locators.password_locators import PasswordLocators
import allure


class PasswordPage(BasePage):
    @allure.step('Клик по кнопке «Восстановить пароль»')
    def click_button_recovery_password(self):
        self.wait_visibility_element(PasswordLocators.BUTTON_RECOVERY_PASSWORD)
        self.click_element(PasswordLocators.BUTTON_RECOVERY_PASSWORD)

    @allure.step('Ввод email')
    def enter_email(self, test_mail):
        self.wait_visibility_element(PasswordLocators.EMAIL)
        self.enter_text(PasswordLocators.EMAIL, test_mail)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_button_recovery(self):
        self.click_element(PasswordLocators.BUTTON_RESTORE)

    @allure.step('Проверить наличие на странице кнопки сохранить')
    def wait_displaying_save(self):
        return self.wait_visibility_element(PasswordLocators.BUTTON_SAVE)

    @allure.step('Клик по иконке открытия пароля')
    def click_icon(self):
        self.click_element(PasswordLocators.ICON_ACTION_PASSWORD)

    @allure.step('Проверить что поле пароль активно')
    def check_active_password(self):
        return self.displaying_element(PasswordLocators.NEW_PASSWORD)

    @allure.step('Получить ссылку текущей страницы')
    def check_url(self):
        return self.get_url()

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_button_personal_account(self):
        self.wait_clickable_element(PasswordLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(PasswordLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Проверить что поле пароль активно')
    def check_active_password(self):
        return self.displaying_element(PasswordLocators.NEW_PASSWORD)