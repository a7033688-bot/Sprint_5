from locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import url, login_endpoint
from data import email, password


class TestTransitionFromPersonalAccountToConstructor:

    def test_transition_from_personal_account_to_constructor(self,driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        driver.find_element(*Locator.button_for_logging_into_account).click()
        driver.find_element(*Locator.click_register_button_in_login_form).click()
        driver.find_element(*Locator.field_for_entering_name_in_registration_form).send_keys('Андрей')
        my_email = email
        my_password = password
        driver.find_element(*Locator.field_for_entering_email_address_in_registration_form).send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((Locator.field_for_entering_password_in_registration_form)))
        element.send_keys(my_password)
        driver.find_element(*Locator.click_register_button_in_registration_form ).click()
        wait.until(EC.url_contains(login_endpoint))
        element= wait.until(EC.presence_of_element_located((Locator.email_field_in_login_form)))
        element.send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((Locator.password_field_in_login_form)))
        element.send_keys(my_password)
        driver.find_element(*Locator.click_login_button_in_login_form).click()
        driver.find_element(*Locator.click_personal_account_button_on_main_page).click()
        driver.find_element(*Locator.constructor_button_in_personal_account).click()
        wait.until(EC.visibility_of_element_located((Locator.click_personal_account_button_on_main_page)))
        current_url = driver.current_url
        assert current_url == url

    def test_transition_from_personal_account_to_logo(self,driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        driver.find_element(*Locator.button_for_logging_into_account).click()
        driver.find_element(*Locator.click_register_button_in_login_form).click()
        driver.find_element(*Locator.field_for_entering_name_in_registration_form).send_keys('Андрей')
        my_email = email
        my_password = password
        driver.find_element(*Locator.field_for_entering_email_address_in_registration_form).send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((Locator.field_for_entering_password_in_registration_form)))
        element.send_keys(my_password)
        driver.find_element(*Locator.click_register_button_in_registration_form).click()
        wait.until(EC.url_contains(login_endpoint))
        element= wait.until(EC.presence_of_element_located((Locator.email_field_in_login_form)))
        element.send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((Locator.password_field_in_login_form)))
        element.send_keys(my_password)
        element= wait.until(EC.element_to_be_clickable((Locator.click_login_button_in_login_form)))
        element.click()
        driver.find_element(*Locator.click_personal_account_button_on_main_page).click()
        element= wait.until(EC.element_to_be_clickable((Locator.logo_in_personal_account)))
        element.click()
        wait.until(EC.visibility_of_element_located((Locator.click_personal_account_button_on_main_page)))
        current_url = driver.current_url
        assert current_url == url