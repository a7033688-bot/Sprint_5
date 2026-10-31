from locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTransitionsBetweenSections:
    
    def test_sauce(self,driver,url):
            wait = WebDriverWait(driver, 10)
            driver.get(url)
            element = wait.until(EC.element_to_be_clickable((Locator.souces_button_in_constructor)))
            element.click()
            wait.until(EC.visibility_of_element_located((Locator.heading_souces)))

    def test_filling(self,driver,url):
            wait = WebDriverWait(driver, 10)
            driver.get(url)
            element = wait.until(EC.element_to_be_clickable((Locator.filling_button_in_constructor)))
            element.click()
            wait.until(EC.visibility_of_element_located((Locator.heading_filling)))

    def test_buns(self,driver,url):
            wait = WebDriverWait(driver, 10)
            driver.get(url)
            element = wait.until(EC.element_to_be_clickable((Locator.bun_button_in_constructor)))
            driver.execute_script("arguments[0].click()", element)
            wait.until(EC.visibility_of_element_located((Locator.heading_bun)))
