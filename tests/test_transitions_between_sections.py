from locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import url

class TestTransitionsBetweenSections:
    
    def test_sauce(self,driver):
            wait = WebDriverWait(driver, 10)
            driver.get(url)
            element = wait.until(EC.element_to_be_clickable((Locator.souces_button_in_constructor)))
            element.click()
            class_atr = wait.until(EC.visibility_of_all_elements_located(Locator.souces_button_in_constructor)).get_attribute("class")
            assert "tab_tab_type_current" in class_atr
            

    def test_filling(self,driver):
            wait = WebDriverWait(driver, 10)
            driver.get(url)
            element = wait.until(EC.element_to_be_clickable((Locator.filling_button_in_constructor)))
            element.click()
            class_atr = wait.until(EC.visibility_of_all_elements_located(Locator.filling_button_in_constructor)).get_attribute("class")
            assert "tab_tab_type_current" in class_atr

    def test_buns(self,driver):
            wait = WebDriverWait(driver, 10)
            driver.get(url)
            element = wait.until(EC.element_to_be_clickable((Locator.bun_button_in_constructor)))
            driver.execute_script("arguments[0].click()", element)
            class_atr = wait.until(EC.visibility_of_all_elements_located(Locator.bun_button_in_constructor)).get_attribute("class")
            assert "tab_tab_type_current" in class_atr
            
