from locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import url, profil_endpoint, login_endpoint
from data import email, password


class TestClickingOnPersonalAccountLeads:

    def test_clicking_on_personal_account_leads(self,driver):
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
        driver.find_element(*Locator.click_login_button_in_login_form).click()
        element = wait.until(EC.visibility_of_element_located((Locator.click_personal_account_button_on_main_page)))
        element.click()
        wait.until(EC.url_contains(profil_endpoint))
        current_url = driver.current_url
        assert profil_endpoint in current_url 