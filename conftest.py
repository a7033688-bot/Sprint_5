import pytest
import random 
from selenium import webdriver


@pytest.fixture
def email():
    login = random.randint(000,999)
    return f'VaulinAndrey52{login}@ya.ru'

@pytest.fixture
def password():
    password = random.randint(000000,999999)
    return password

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit

@pytest.fixture
def url():
    return 'https://qa-stellarburgers.education-services.ru/'