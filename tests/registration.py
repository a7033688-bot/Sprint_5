from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:

    def test_registration_with_valid_data(self,email,password):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get('https://qa-stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH,'.//button[contains(text(),"Войти в аккаунт")]').click()
        driver.find_element(By.XPATH,'.//a[contains(text(),"Зарегистрироваться")]').click()
        driver.find_element(By.XPATH,'.//label[text()="Имя"]/following-sibling::input').send_keys('Андрей')
        my_email = email
        my_password = password
        driver.find_element(By.XPATH,'.//label[text()="Email"]/following-sibling::input').send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((By.XPATH,'.//label[text()="Пароль"]/following-sibling::input')))
        element.send_keys(my_password)
        driver.find_element(By.XPATH,'.//button[contains(text(),"Зарегистрироваться")]').click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login'
        driver.quit()

    def test_error_incorrect_password(self,email):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get('https://qa-stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH,'.//button[contains(text(),"Войти в аккаунт")]').click()
        driver.find_element(By.XPATH,'.//a[contains(text(),"Зарегистрироваться")]').click()
        driver.find_element(By.XPATH,'.//label[text()="Имя"]/following-sibling::input').send_keys('Андрей')
        my_email = email
        driver.find_element(By.XPATH,'.//label[text()="Email"]/following-sibling::input').send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((By.XPATH,'.//label[text()="Пароль"]/following-sibling::input')))
        element.send_keys('12345')
        driver.find_element(By.XPATH,'.//button[contains(text(),"Зарегистрироваться")]').click()
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/login' , f'Не переходит на страницу входа из-за некоректного пароля'
        driver.quit()