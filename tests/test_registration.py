from locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:

    def test_registration_with_valid_data(self,driver,url,email,password):
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        driver.find_element(*Locator.button_for_logging_into_account).click()
        driver.find_element(*Locator.click_register_button_in_login_form).click()
        element = wait.until(EC.visibility_of_element_located((Locator.field_for_entering_name_in_registration_form)))
        element.send_keys('Андрей')
        my_email = email
        my_password = password
        driver.find_element(*Locator.field_for_entering_email_address_in_registration_form).send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((Locator.field_for_entering_password_in_registration_form)))
        element.send_keys(my_password)
        driver.find_element(*Locator.click_register_button_in_registration_form).click()
        wait.until(EC.url_contains('/login'))
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'

    def test_error_incorrect_password(self,driver,url,email):
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        driver.find_element(*Locator.button_for_logging_into_account).click()
        driver.find_element(*Locator.click_register_button_in_login_form).click()
        element = wait.until(EC.visibility_of_element_located((Locator.field_for_entering_name_in_registration_form)))
        element.send_keys('Андрей')
        my_email = email
        driver.find_element(*Locator.field_for_entering_email_address_in_registration_form).send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((Locator.field_for_entering_password_in_registration_form)))
        element.send_keys('12345')
        driver.find_element(*Locator.click_register_button_in_registration_form).click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login' , f'Не переходит на страницу входа из-за некоректного пароля'