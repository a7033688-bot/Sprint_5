from locators import Locator


class TestEntrance:
    def test_log_your_account_button(self,driver,url):
        driver.get(url)
        driver.find_element(*Locator.button_for_logging_into_account).click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'

    def test_button_personal_account(self,driver,url):
        driver.get(url)
        driver.find_element(*Locator.click_personal_account_button_on_main_page).click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'

    def test_log_in_using_button_in_registration_form(self,driver,url):
        driver.get(url)
        driver.find_element(*Locator.button_for_logging_into_account).click()
        driver.find_element(*Locator.click_register_button_in_login_form).click()
        driver.find_element(*Locator.login_button_is_located_in_registration_form).click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'

    def test_log_in_to_system_using_button_in_password_recovery_form(self,driver,url):
        driver.get(url)
        driver.find_element(*Locator.button_for_logging_into_account).click()
        driver.find_element(*Locator.click_forgot_password_button_in_login_form).click()
        driver.find_element(*Locator.login_button_is_located_in_registration_form).click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'

