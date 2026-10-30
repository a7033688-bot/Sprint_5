from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTransitionsBetweenSections:
    
    def test_sauce(self):
            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 10)
            driver.get('https://qa-stellarburgers.education-services.ru/')
            element = wait.until(EC.element_to_be_clickable((By.XPATH, ".//span[text()='Соусы']/parent::div")))
            element.click()
            wait.until(EC.visibility_of_element_located((By.XPATH,'.//h2[text()="Соусы"]')))
            driver.quit()

    def test_filling(self):
            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 10)
            driver.get('https://qa-stellarburgers.education-services.ru/')
            element = wait.until(EC.element_to_be_clickable((By.XPATH, ".//span[text()='Начинки']/parent::div")))
            element.click()
            driver.find_element(By.XPATH, ".//span[text()='Начинки']/parent::div").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,'.//h2[text()="Начинки"]')))
            driver.quit()

    def test_buns(self):
            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 10)
            driver.get('https://qa-stellarburgers.education-services.ru/')
            element = wait.until(EC.element_to_be_clickable((By.XPATH, ".//span[text()='Булки']/parent::div")))
            driver.execute_script("arguments[0].click()", element)
            wait.until(EC.visibility_of_element_located((By.XPATH,'.//h2[text()="Булки"]')))
            driver.quit()
