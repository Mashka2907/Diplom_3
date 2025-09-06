from pages.personal_account_page import PersonalAccountPage
from conftest import driver
import allure
from urls import Urls


@allure.feature('Личный кабинет')
class TestPersonalAccount:
    @allure.title('Переход по клику на "Личный кабинет"')
    def test_personal_account(self, driver, create_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_to_account(create_user)
        personal_account_page.click_button_personal_account()
        personal_account_page.wait_button_profile()

        assert personal_account_page.get_url() == Urls.PROFILE

    @allure.title('Переход в раздел "История заказов"')
    def test_order_history(self, driver, create_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_to_account(create_user)
        personal_account_page.click_button_personal_account()
        personal_account_page.click_history_order()

        assert personal_account_page.get_url() == Urls.HISTORY_ORDER

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, create_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_to_account(create_user)
        personal_account_page.click_button_personal_account()
        personal_account_page.click_exit()

        assert personal_account_page.get_url() == Urls.PROFILE