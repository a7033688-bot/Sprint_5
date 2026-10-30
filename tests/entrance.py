from selenium import webdriver
from selenium.webdriver.common.by import By


class TestEntrance:
    def test_log_your_account_button(self):
        driver = webdriver.Chrome()
        driver.get('https://qa-stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH,'.//button[contains(text(),"Войти в аккаунт")]').click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'
        driver.quit()

    def test_button_personal_account(self):
        driver = webdriver.Chrome()
        driver.get('https://qa-stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH,'.//p[contains(text(),"Личный Кабинет")]').click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'
        driver.quit()

    def test_log_in_using_button_in_registration_form(self):
        driver = webdriver.Chrome()
        driver.get('https://qa-stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH,'.//button[contains(text(),"Войти в аккаунт")]').click()
        driver.find_element(By.XPATH,'.//a[contains(text(),"Зарегистрироваться")]').click()
        driver.find_element(By.XPATH,'.//a[contains(text(),"Войти")]').click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'
        driver.quit()

    def test_log_in_to_system_using_button_in_password_recovery_form(self):
        driver = webdriver.Chrome()
        driver.get('https://qa-stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH,'.//button[contains(text(),"Войти в аккаунт")]').click()
        driver.find_element(By.XPATH,'.//a[contains(text(),"Восстановить пароль")]').click()
        driver.find_element(By.XPATH,'.//a[contains(text(),"Войти")]').click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'
        driver.quit()

