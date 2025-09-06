from pages.password_page import PasswordPage
from conftest import driver
import allure
from urls import Urls
from data import Data


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_click_button_password_recovery(self, driver):
        password_recovery = PasswordPage(driver)
        password_recovery.click_button_personal_account()
        password_recovery.click_button_recovery_password()

        assert password_recovery.get_url() == Urls.FORGOT_PASSWORD


    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_click_button_recovery(self, driver):
        password_recovery = PasswordPage(driver)
        password_recovery.click_button_personal_account()
        password_recovery.click_button_recovery_password()

        password_recovery.enter_email(Data.email)
        password_recovery.click_button_recovery()
        password_recovery.wait_displaying_save()

        assert password_recovery.get_url() == Urls.RESET_PASSWORD


    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_is_active(self, driver):
        password_recovery = PasswordPage(driver)
        password_recovery.click_button_personal_account()
        password_recovery.click_button_recovery_password()
        password_recovery.enter_email(Data.email)
        password_recovery.click_button_recovery()
        password_recovery.click_icon()

        assert password_recovery.check_active_password()