import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTransitionFromPersonalAccountToConstructor:

    def test_transition_from_personal_account_to_constructor(self,email,password):
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
        time.sleep(2)
        element= wait.until(EC.presence_of_element_located((By.XPATH,'.//input[@type="text" and @name="name"]')))
        element.send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((By.XPATH,'.//input[@type="password" and @name="Пароль"]')))
        element.send_keys(my_password)
        driver.find_element(By.XPATH,'.//button[contains(text(),"Войти")]').click()
        driver.find_element(By.XPATH,'.//p[contains(text(),"Личный Кабинет")]').click()
        driver.find_element(By.XPATH,'.//p[contains(text(),"Конструктор")]').click()
        time.sleep(2)
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/'
        driver.quit()

    def test_transition_from_personal_account_to_logo(self,email,password):
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
        time.sleep(2)
        element= wait.until(EC.presence_of_element_located((By.XPATH,'.//input[@type="text" and @name="name"]')))
        element.send_keys(my_email)
        element = wait.until(EC.presence_of_element_located((By.XPATH,'.//input[@type="password" and @name="Пароль"]')))
        element.send_keys(my_password)
        element= wait.until(EC.element_to_be_clickable((By.XPATH,'.//button[contains(text(),"Войти")]')))
        element.click()
        driver.find_element(By.XPATH,'.//p[contains(text(),"Личный Кабинет")]').click()
        element= wait.until(EC.element_to_be_clickable((By.XPATH,'//div[contains(@class,"header__logo")]//a')))
        element.click()
        time.sleep(2)
        current_url = driver.current_url
        assert current_url == 'https://qa-stellarburgers.education-services.ru/'
        driver.quit()