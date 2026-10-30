import pytest
import random 


@pytest.fixture
def email():
    login = random.randint(000,999)
    return f'VaulinAndrey52{login}@ya.ru'

@pytest.fixture
def password():
    password = random.randint(000000,999999)
    return password